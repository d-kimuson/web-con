<script lang="ts">
  import { onMount } from "svelte"
  import { isMuteStore, isVideoOnStore } from "@svelte/store"

  // Component Props
  export let videoSrc: MediaStream | null
  export let isMute: boolean = false
  export let isVideoOn: boolean = false
  export let isMenu: boolean = true
  export let isLocal: boolean = false

  if (isLocal) {
    // 自分用 SteramVideo は LocalStorage と同期する
    isMute = isMuteStore.get()
    isVideoOn = isVideoOnStore.get()
  }

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
    videoTracks[0].enabled = isVideoOn

    if (isLocal) {
      isVideoOnStore.set(isVideoOn)
    }
  }

  function onMuteChange() {
    const audioTracks = videoSrc?.getAudioTracks()

    if (!audioTracks) return
    audioTracks[0].enabled = !isMute

    if (isLocal) {
      isMuteStore.set(isMute)
    }
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
  <!-- svelte-ignore a11y-media-has-caption -->
  <video muted={isLocal} bind:this={videoElement} />
  {#if isMenu}
    <div class="menu-container">
      <!-- いずれアイコン等でわかりやすく、とりあえず機能だけ -->
      <label> <input type="checkbox" bind:checked={isMute} /> ミュート </label>
      <label> <input type="checkbox" bind:checked={isVideoOn} /> ビデオ </label>
    </div>
  {/if}
</div>
