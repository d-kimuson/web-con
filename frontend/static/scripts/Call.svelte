<script lang="ts">
  import Peer, { SfuRoom } from "skyway-js"
  import { onMount } from 'svelte'
  import dayjs from "dayjs"

  import { loginUser, roomDetail } from "@scripts/api"
  import AsyncStreamVideo from "@scripts/components/AsyncStreamVideo.svelte"
  import StreamVideo from "@scripts/components/StreamVideo.svelte"
  import Chat from "@scripts/components/Chat.svelte"

  // Variables
  const roomMode = `sfu`
  const roomKey = `7ddc9b1a-aac8-4f60-a5f8-bc8703c3a125`

  const url = new URL(location.href)
  const roomId = url.pathname.split(`/`).slice(-1)[0]

  let peer: Peer | undefined
  let user: UserSerializer | undefined
  let localStream = getLocalStream()
  let room: SfuRoom

  let localStreamElement: AsyncStreamVideo
  let chatElement: Chat
  let self: User

  interface RoomMember {
    name: string
    userId: string
    stream: MediaStream
    video: StreamVideo | null
  }

  let roomMembers: RoomMember[] = []
  let roomInfo = roomDetail(roomId)
  let isJoin = false

  // ページロード時
  onMount(async () => {
    // ログインユーザー情報の取得
    const response = await loginUser()

    if (!response) {
      // TODO: ログインページへの誘導などしたほうが良い
      alert(`ログイン状態を確認してください`)
      return
    }

    user = response

    // 接続用 Peer の準備
    // TODO: skyway 側で 登録済みユーザー以外の参加を弾く必要がある
    peer = new Peer(user.pk, {
      key: roomKey,
      debug: 3,
    })

    const actualLocalStream = await localStream

    // リロード 自動で再接続
    if (localStorage.getItem(`isJoin`) === `true` &&
        localStorage.getItem(`currentRoom`) === roomId &&
        actualLocalStream && user && peer) {

      // peer が開くまで待つ
      let count = 0
      const tid = setInterval(async () => {
        if (count > 5) {
          // 5秒でタイムアウト
          clearInterval(tid)
        }

        if (user && peer && peer.open) {
          // peer が開いたのを確認して参加する

          clearInterval(tid)
          try {
            join({ user, peer, localStream: actualLocalStream })
          } catch (error) {
            console.log(`ERROR`, error)
          }
        }

        count++
        console.log(`${count} 秒たった`)
      }, 1000)
    }
  })

  // Functions
  async function getLocalStream(): Promise<MediaStream | null> {
    return navigator.mediaDevices
      .getUserMedia({
        audio: true,
        video: true,
      })
      .catch((): null => {
        alert(`カメラとマイクを許可してください`)
        return null
      })
  }

  async function checkAndJoin() {
    const actualLocalStream = await localStream
    if (!actualLocalStream) {
      alert(`カメラとマイクに問題があります`)
      return
    }

    if (!peer) {
      alert(`参加準備が整っていません`)
      console.log(`because peer is undefined`)
      return
    }

    if (!peer.open) {
      alert(`参加準備が整っていません`)
      console.log(`because peer is not open`)
      return
    }

    if (!user) {
      alert(`ログイン状態を確認してください`)
      return
    }

    join({user, peer, localStream: actualLocalStream})
  }

  async function join({ user, peer, localStream }: { user: UserSerializer, peer: Peer, localStream: MediaStream }) {
    self = {
      name: user.email,
      userId: user.pk,
    }
    isJoin = true

    room = peer.joinRoom<SfuRoom>(roomId, {
      mode: roomMode,
      stream: localStream,
    })

    localStorage.setItem(`isJoin`, `true`)
    localStorage.setItem(`currentRoom`, roomId)

    // イベントハンドリング
    room.once(`open`, () => chatElement.writeLog(`参加しました！`))

    room.on(`peerJoin`, (peerId) => {
      const member = getMember(peerId)
      chatElement.writeLog(`${member ? member.name : peerId} が参加しました！`)
    })

    room.on(`stream`, async (stream) => {
      const member = getMember(stream.peerId)

      if (member) {
        member.stream = stream
      } else {
        const roomUser = (await roomInfo)?.room_members.find(
          (roomMember) => (roomMember.user.pk = stream.peerId)
        )

        if (roomUser) {
          roomMembers = [
            ...roomMembers,
            {
              name: roomUser.user.email,
              userId: roomUser.user.pk,
              stream: stream,
              video: null,
            },
          ]
        }
      }
    })

    room.on(`data`, ({ data, src }) => {
      // 他ユーザーから data (チャット) が書き込まれた
      const member = getMember(src)

      if (typeof member !== `undefined`) {
        chatElement.reveiveMessage(
          {
            name: member.name,
            userId: member.userId,
          },
          data,
        )
      }
    })

    room.on(`peerLeave`, (peerId) => {
      console.log("peerLeave is called")
      const member = getMember(peerId)
      if (member?.video && member?.video !== null) {
        console.log("null: ", member.video)
        member.video.remove()
      }
      roomMembers = roomMembers.filter((member) => member.userId !== peerId)

      chatElement.writeLog(`${member ? member.name : peerId} が退出しました`)
    })

    room.once(`close`, () => {
      chatElement.writeLog(`退出しました`)
      localStorage.setItem(`isJoin`, `false`)
      localStorage.removeItem(`currentRoom`)

      roomMembers.forEach((roomMember) => {
        roomMember.video?.remove()
      })

      moveToCompletePage()
    })

    // 自動退出
    const now = dayjs()
    const endTime = (await roomInfo)?.end_datetime

    if (endTime) {
      // 残り時間によっては、setTimeout の最大時間を超えてしまうので。
      // とりあえず最大でも5時間を想定する
      const remainingTime = Math.min(endTime.diff(now), 5 * 60 * 60 * 1000)

      setTimeout(() => {
        moveToCompletePage()
      }, remainingTime);
    }
  }

  function leave() {
    room.close()
  }

  function getMember(id: string): RoomMember | undefined {
    return roomMembers.find((member) => member.userId === id)
  }

  function moveToCompletePage() {
    window.location.href = `/completed_call`
  }
</script>

<style lang="scss">
  .videos-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }

  .local-video-container {
    // 見分けがつくように仮で外枠に色をつけておく
    border: solid 10px green;
  }
</style>

<div>
  <div class="room">
    <div>
      {#if !isJoin}
        <button on:click={checkAndJoin}>参加する</button>
      {:else}<button on:click={leave}>退席する</button>{/if}
    </div>

    <div class="videos-container">
      <div class="local-video-container">
        <AsyncStreamVideo
          isLocal={true}
          videoSrc={localStream}
          isMute={true}
          bind:this={localStreamElement} />
      </div>
      {#each roomMembers as roomMember, index}
        <StreamVideo
          videoSrc={roomMember.stream}
          isLocal={false}
          isMute={true}
          bind:this={roomMembers[index].video} />
      {/each}
    </div>

    {#if room}
      <Chat {self} {room} bind:this={chatElement} />
    {/if}
  </div>
  <p class="meta" id="js-meta" />
</div>
