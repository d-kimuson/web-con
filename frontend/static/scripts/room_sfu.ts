import Peer, { SfuRoom } from "skyway-js"
import { getElementById } from "@scripts/util"

const stopMediaStream = async (
  element: HTMLVideoElement | null,
): Promise<void> => {
  const videoSrc = element?.srcObject

  if (videoSrc && `getTracks` in videoSrc) {
    videoSrc.getTracks().forEach((track) => track.stop())
  }

  if (element !== null) {
    element.srcObject = null
    element.remove()
  }
}

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
  const localVideoElement = <HTMLVideoElement>getElementById(`js-local-stream`)
  const remoteVideoElements = getElementById(`js-remote-streams`)
  const chatInputElement = <HTMLInputElement>getElementById(`js-local-text`)
  const sendButton = getElementById(`js-send-trigger`)
  const joinButton = getElementById(`js-join-trigger`)
  const leaveButton = getElementById(`js-leave-trigger`)
  const chatContainer = getElementById(`js-messages`)

  // local stream (カメラとマイクのストリーム)
  const localStream = await navigator.mediaDevices
    .getUserMedia({
      audio: true,
      video: true,
    })
    .catch(() => alert(`カメラとマイクを許可してください`))

  if (localStream) {
    localVideoElement.muted = true
    localVideoElement.srcObject = localStream
    localVideoElement.playsInline = true
    await localVideoElement.play().catch(console.error)
  }

  // ボタンのハンドリング
  joinButton.addEventListener(`click`, () => {
    if (!peer.open) {
      alert(`参加準備が整っていません`)
      return
    }

    if (!localStream) {
      alert(`カメラとマイクに問題があります`)
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
      const newVideo = document.createElement(`video`)
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
      const targetVideoElement = remoteVideoElements.querySelector<
        HTMLVideoElement
      >(`[data-peer-id="${peerId}"]`)
      stopMediaStream(targetVideoElement)

      chatContainer.textContent += `=== ${peerId} left ===\n`
    })

    room.once(`close`, () => {
      // 自分がルームを退出
      sendButton.removeEventListener(`click`, onClickSend)
      chatContainer.textContent += `== You left ===\n`
      const videoElemnts = <HTMLVideoElement[]>(
        Array.from(remoteVideoElements.children)
      )

      videoElemnts.forEach((videoElement) => stopMediaStream(videoElement))
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
