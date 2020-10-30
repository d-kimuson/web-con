import Peer from "skyway-js"

interface VideoElement extends HTMLVideoElement {
  playsInline: boolean
}

const getElementById = (id: string) => {
  const elm = document.getElementById(id)
  if (elm !== null) {
    return elm
  } else {
    throw new Error(`HTMLElemet: id=${id}が存在しません`)
  }
}

;(async () => {
  const url = new URL(location.href)
  const roomId = url.pathname.split(`/`).slice(-1)[0]
  const roomMode = `sfu`

  const peer = new Peer({
    key: `7ddc9b1a-aac8-4f60-a5f8-bc8703c3a125`,
    debug: 3,
  })

  const localVideo = <VideoElement>getElementById(`js-local-stream`)
  const remoteVideos = getElementById(`js-remote-streams`)

  const localText = <HTMLInputElement>getElementById(`js-local-text`)

  const joinTrigger = getElementById(`js-join-trigger`)
  const leaveTrigger = getElementById(`js-leave-trigger`)

  const sendTrigger = getElementById(`js-send-trigger`)
  const messages = getElementById(`js-messages`)

  const localStream = <MediaStream>await navigator.mediaDevices
    .getUserMedia({
      audio: true,
      video: true,
    })
    .catch(console.error)

  localVideo.muted = true
  localVideo.srcObject = localStream
  localVideo.playsInline = true

  await localVideo.play().catch(console.error)

  joinTrigger.addEventListener(`click`, () => {
    if (!peer.open) {
      return
    }

    const room = peer.joinRoom(roomId, {
      mode: roomMode,
      stream: localStream,
    })

    room.once(`open`, () => {
      messages.textContent += `=== You joined ===\n`
    })
    room.on(`peerJoin`, (peerId) => {
      messages.textContent += `=== ${peerId} joined ===\n`
    })

    // Render remote stream for new peer join in the room
    room.on(`stream`, async (stream) => {
      const newVideo = <VideoElement>document.createElement(`video`)
      newVideo.srcObject = stream
      newVideo.playsInline = true
      newVideo.setAttribute(`data-peer-id`, stream.peerId)
      remoteVideos.append(newVideo)
      await newVideo.play().catch(console.error)
    })

    room.on(`data`, ({ data, src }) => {
      messages.textContent += `${src}: ${data}\n`
    })

    room.on(`peerLeave`, (peerId) => {
      const remoteVideo = <VideoElement>(
        remoteVideos.querySelector(`[data-peer-id="${peerId}"]`)
      )
      const videoSrc = <MediaStream>remoteVideo.srcObject
      videoSrc.getTracks().forEach((track) => track.stop())
      remoteVideo.srcObject = null
      remoteVideo.remove()

      messages.textContent += `=== ${peerId} left ===\n`
    })

    room.once(`close`, () => {
      sendTrigger.removeEventListener(`click`, onClickSend)
      messages.textContent += `== You left ===\n`
      const videoElemnts = <VideoElement[]>Array.from(remoteVideos.children)

      videoElemnts.forEach((videoElement) => {
        const videoSrc = <MediaStream>videoElement.srcObject
        videoSrc.getTracks().forEach((track) => track.stop())
        videoElement.srcObject = null
        videoElement.remove()
      })
    })

    sendTrigger.addEventListener(`click`, onClickSend)
    leaveTrigger.addEventListener(`click`, () => room.close(), { once: true })

    function onClickSend() {
      room.send(localText.value)

      messages.textContent += `${peer.id}: ${localText.value}\n`
      localText.value = ``
    }
  })

  peer.on(`error`, console.error)
})()
