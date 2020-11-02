<script lang="ts">
  import { onMount } from "svelte"

  // Component Props
  export let videoSrc: MediaStream | null
  export let isMute: boolean = false

  // Local Variables
  let videoElement: HTMLVideoElement

  // Component Functions
  export async function start(): Promise<void> {
    await videoElement.play().catch(console.error)
  }

  export async function stop(): Promise<void> {
    if (videoSrc && `getTracks` in videoSrc) {
      videoSrc.getTracks().forEach((track) => track.stop())
    }
  }

  export async function remove(): Promise<void> {
    await stop()
    if (videoSrc !== null) {
      videoElement.srcObject = null
      videoElement.remove()
    }
  }

  // Component Local Functions
  onMount(async () => {
    videoElement.srcObject = videoSrc
    videoElement.playsInline = true
    start()
  })
</script>

<video muted={isMute} bind:this={videoElement} />
