<script lang="ts">
  import { onMount } from "svelte"

  // Component Props
  export let videoSrc: MediaStream | null
  export let isMute: boolean = false
  export let isVideoOn: boolean = false
  export const isMenu: boolean = true

  // Local Variables
  let videoElement: HTMLVideoElement

  // Watch
  $: ((mute: boolean) => onMuteChange())(isMute)
  $: ((video: boolean) => onVideoChange())(isVideoOn)

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
    }
  }

  // Component Local Functions
  function onVideoChange() {
    const videoTracks = videoSrc?.getVideoTracks()

    if (!videoTracks) return
    videoTracks[0].enabled = !isVideoOn
  }

  function onMuteChange() {
    const audioTracks = videoSrc?.getAudioTracks()

    if (!audioTracks) return
    audioTracks[0].enabled = !isMute
  }

  // Application
  onMount(async () => {
    videoElement.srcObject = videoSrc
    videoElement.playsInline = true
    await start()
  })
</script>

<style lang="scss">
  $-menu-height: 50px;

  .video-wrapper {
    position: relative;
  }

  .menu-container {
    position: absolute;
    top: calc(100% - #{$-menu-height});
    left: 0;
    height: $-menu-height;
    width: 100%;
    background: white;
  }
</style>

<div class="video-wrapper">
  <video bind:this={videoElement} />
  {#if isMenu}
    <div class="menu-container">
      <!-- いずれアイコン等でわかりやすく、とりあえず機能だけ -->
      <label> <input type="checkbox" bind:checked={isMute} /> ミュート </label>
      <label> <input type="checkbox" bind:checked={isVideoOn} /> ビデオ </label>
    </div>
  {/if}
</div>
