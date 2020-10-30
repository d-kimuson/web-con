import Peer, { SfuRoom } from "skyway-js"
import { VideoElement, getElementById } from "@scripts/util"

export const setupSfuRoom = async (): Promise<void> => {
  const roomMode = `sfu`
  const roomKey = `7ddc9b1a-aac8-4f60-a5f8-bc8703c3a125`

  // setup
  const url = new URL(location.href)
  const roomId = url.pathname.split(`/`).slice(-1)[0]
  const peer = new Peer({
    key: roomKey,
    debug: 3,
  })

  // handled elements
  const localVideoElement = <VideoElement>getElementById(`js-local-stream`)
  const remoteVideoElements = getElementById(`js-remote-streams`)
  const chatInputElement = <HTMLInputElement>getElementById(`js-local-text`)
  const sendButton = getElementById(`js-send-trigger`)
  const joinButton = getElementById(`js-join-trigger`)
  const leaveButton = getElementById(`js-leave-trigger`)
  const chatContainer = getElementById(`js-messages`)

  // local stream (カメラとマイクのストリーム)
  const localStream = <MediaStream>await navigator.mediaDevices
    .getUserMedia({
      audio: true,
      video: true,
    })
    .catch(() => alert(`カメラとマイクを許可してください`))

  localVideoElement.muted = true
  localVideoElement.srcObject = localStream
  localVideoElement.playsInline = true
  await localVideoElement.play().catch(console.error)

  // ボタンのハンドリング
  joinButton.addEventListener(`click`, () => {
    if (!peer.open) {
      return
    }

    const room = peer.joinRoom<SfuRoom>(roomId, {
      mode: roomMode,
      stream: localStream,
    })

    // イベントハンドリング
    room.once(`open`, () => {
      // ルームに自分が参加
      chatContainer.textContent += `=== You joined ===\n`
    })
    room.on(`peerJoin`, (peerId) => {
      // 他 peer (ユーザー)がルームに参加
      chatContainer.textContent += `=== ${peerId} joined ===\n`
    })

    room.on(`stream`, async (stream) => {
      // 他ユーザーのストリームが追加
      const newVideo = <VideoElement>document.createElement(`video`)
      newVideo.srcObject = stream
      newVideo.playsInline = true
      newVideo.setAttribute(`data-peer-id`, stream.peerId)
      remoteVideoElements.append(newVideo)
      await newVideo.play().catch(console.error)
    })

    room.on(`data`, ({ data, src }) => {
      // 他ユーザーから data(チャット) が書き込まれた
      chatContainer.textContent += `${src}: ${data}\n`
    })

    room.on(`peerLeave`, (peerId) => {
      // 他 peer(ユーザー)がルームを退出
      const remoteVideo = <VideoElement>(
        remoteVideoElements.querySelector(`[data-peer-id="${peerId}"]`)
      )
      const videoSrc = <MediaStream>remoteVideo.srcObject
      videoSrc.getTracks().forEach((track) => track.stop())
      remoteVideo.srcObject = null
      remoteVideo.remove()

      chatContainer.textContent += `=== ${peerId} left ===\n`
    })

    room.once(`close`, () => {
      // 自分がルームを退出
      sendButton.removeEventListener(`click`, onClickSend)
      chatContainer.textContent += `== You left ===\n`
      const videoElemnts = <VideoElement[]>(
        Array.from(remoteVideoElements.children)
      )

      videoElemnts.forEach((videoElement) => {
        const videoSrc = <MediaStream>videoElement.srcObject
        videoSrc.getTracks().forEach((track) => track.stop())
        videoElement.srcObject = null
        videoElement.remove()
      })
    })

    sendButton.addEventListener(`click`, onClickSend)
    leaveButton.addEventListener(`click`, () => room.close(), { once: true })

    function onClickSend() {
      room.send(chatInputElement.value)

      chatContainer.textContent += `${peer.id}: ${chatInputElement.value}\n`
      chatInputElement.value = ``
    }
  })

  peer.on(`error`, console.error)
}
