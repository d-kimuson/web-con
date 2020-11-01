import { setupSfuRoom } from "@scripts/room_sfu"
import CallApp from "@scripts/Call.svelte"

import { getElementById } from "@scripts/util"

setupSfuRoom()

const callApp = new CallApp({
  target: getElementById(`svelte`),
  props: {
    name: `Taro`,
  },
})

export default callApp
