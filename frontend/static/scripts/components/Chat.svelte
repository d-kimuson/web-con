<script lang="ts">
  import type { SfuRoom } from "skyway-js"
  import dayjs from "dayjs"

  interface User {
    name: string
    userId: string
    peerId: string
  }

  interface Chat {
    user: User
    content: string
  }

  interface Log {
    time: dayjs.Dayjs
    content: string
  }

  // Component Props
  export let self: User
  export let room: SfuRoom

  // Local Variables
  let message: string = ``
  let chatLogs: (Chat | Log)[] = []

  // Component Functions
  export function reveiveMessage(user: User, content: string) {
    writeChat(user, content)
  }

  export function writeLog(content: string) {
    updateLog({
      time: dayjs(new Date()).locale(`Asia/Tokyo`),
      content,
    })
  }

  // Component Local Functions
  function onClickSend() {
    room.send(message)
    writeChat(self, message)

    message = ``
  }

  function writeChat(user: User, content: string) {
    updateLog({
      user,
      content
    })
  }

  function updateLog(target: Chat | Log) {
    chatLogs = [
      ...chatLogs,
      target
    ]
  }
</script>

<style lang="scss">
  .chat-container {
    display: flex;
    flex-direction: column;
  }
</style>

<div>
  <form on:submit={(e) => e.preventDefault()}>
    <input type="text" bind:value={message} />
    <button on:click={onClickSend}>Send</button>
  </form>

  <div class="chat-container">
    {#each chatLogs as log}
      {#if `user` in log}
        <p>{log.user.name}: {log.content}</p>
      {:else}
        <p>{log.time.format(`YYYY年MM月DD日`)}: {log.content}</p>
      {/if}
    {/each}
  </div>
</div>
