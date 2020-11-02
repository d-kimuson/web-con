import CallApp from "@scripts/Call.svelte"

import { getElementById } from "@scripts/util"

const callApp = new CallApp({
  target: getElementById(`svelte`),
})

export default callApp
