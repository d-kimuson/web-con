<script lang="ts">
  import Peer, { SfuRoom } from "skyway-js"
  import AsyncStreamVideo from "@scripts/components/AsyncStreamVideo.svelte"
  import StreamVideo from "@scripts/components/StreamVideo.svelte"
  import Chat from "@scripts/components/Chat.svelte"

  // Variables
  const roomMode = `sfu`
  const roomKey = `7ddc9b1a-aac8-4f60-a5f8-bc8703c3a125`

  const url = new URL(location.href)
  const roomId = url.pathname.split(`/`).slice(-1)[0]
  const peer = new Peer({
    key: roomKey,
    debug: 3,
  })

  let localStream = getLocalStream()
  let room: SfuRoom

  let localStreamElement: AsyncStreamVideo
  let chatElement: Chat

  interface RoomMember {
    name: string
    userId: string
    peerId: string
    stream: MediaStream
    video: StreamVideo | null
  }

  let roomMembers: RoomMember[] = []
  let isJoin = false

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

  async function join() {
    if (!peer.open) {
      alert(`参加準備が整っていません`)
      return
    }

    const actualLocalStream = await localStream
    if (!actualLocalStream) {
      alert(`カメラとマイクに問題があります`)
      return
    }

    isJoin = true

    room = peer.joinRoom<SfuRoom>(roomId, {
      mode: roomMode,
      stream: actualLocalStream,
    })

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
        roomMembers = [
          ...roomMembers,
          {
            name: `名無しくん`,
            userId: `xxx`,
            peerId: stream.peerId,
            stream: stream,
            video: null,
          },
        ]
      }
    })

    room.on(`data`, ({ data, src }) => {
      // 他ユーザーから data (チャット) が書き込まれた
      const member = getMember(src)

      if (typeof member !== `undefined`) {
        chatElement.reveiveMessage(
          {
            name: member.name,
            peerId: member.peerId,
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
      roomMembers = roomMembers.filter((member) => member.peerId !== peerId)

      chatElement.writeLog(`${member ? member.name : peerId} が退出しました`)
    })

    room.once(`close`, () => {
      chatElement.writeLog(`退出しました`)

      roomMembers.forEach((roomMember) => {
        roomMember.video?.remove()
      })


      window.location.href = `/completed_call`
    })
  }

  function leave() {
    room.close()
  }

  function getMember(id: string): RoomMember | undefined {
    return roomMembers.find((member) => member.peerId === id)
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
        <button on:click={join}>参加する</button>
      {:else}<button on:click={leave}>退席する</button>{/if}
    </div>

    <div class="videos-container">
      <div class="local-video-container">
        <AsyncStreamVideo
          videoSrc={localStream}
          isMute={true}
          bind:this={localStreamElement} />
      </div>
      {#each roomMembers as roomMember, index}
        <StreamVideo
          videoSrc={roomMember.stream}
          isMute={true}
          bind:this={roomMembers[index].video} />
      {/each}
    </div>

    {#if room}
      <Chat
        self={{ name: '自分の名前', userId: 'xxx', peerId: peer.id }}
        {room}
        bind:this={chatElement} />
    {/if}
  </div>
  <p class="meta" id="js-meta" />
</div>
