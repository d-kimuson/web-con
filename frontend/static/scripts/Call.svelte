<script lang="ts">
  import Peer, { SfuRoom } from "skyway-js"
  import AsyncVideo from "@scripts/components/AsyncStreamVideo.svelte"
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

  let localStreamElement: StreamVideo
  let chatElement: Chat

  interface RoomMember {
    name: string
    userId: string
    peerId: string
    stream: MediaStream
    video: StreamVideo | null
  }

  let roomMembers: RoomMember[] = []

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
      const member = getMember(peerId)
      member?.video?.remove()
      member?.name
      roomMembers = roomMembers.filter((member) => member.peerId !== peerId)

      chatElement.writeLog(`${member ? member.name : peerId} が退出しました`)
    })

    room.once(`close`, () => {
      localStreamElement.remove()
      chatElement.writeLog(`退出中です`)

      roomMembers.forEach((roomMember) => {
        roomMember.video?.remove()
      })
    })
  }

  function leave() {
    room.close(), { once: true }
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
      <button on:click={join}>参加する</button>
      <button on:click={leave}>一次退席する</button>
    </div>

    <div class="videos-container">
      <div class="local-video-container">
        <AsyncVideo videoSrc={localStream} isMute={true} />
      </div>
      {#each roomMembers as roomMember, index}
        <StreamVideo videoSrc={roomMember.stream} isMute={true} />
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
