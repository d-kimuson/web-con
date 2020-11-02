<script lang="ts">
  import StreamVideo from "@scripts/components/StreamVideo.svelte"

  // Component Props
  export let videoSrc: Promise<MediaStream | null>
  export let isMute: boolean = false

  // Local Variables
  let videoElement: StreamVideo

  // Component Functions
  export async function start(): Promise<void> {
    videoElement.start()
  }

  export async function stop(): Promise<void> {
    videoElement.stop()
  }

  export async function remove(): Promise<void> {
    videoElement.remove()
  }
</script>

<div>
  {#await videoSrc}
    <div>Loading...</div>
  {:then value}
    <StreamVideo isMute={isMute} videoSrc={value} bind:this={videoElement} />
  {:catch error}
    <p>{error.message}</p>
  {/await}
</div>
