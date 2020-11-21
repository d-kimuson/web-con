import CallApp from "@svelte/entries/Call.svelte"

import { getElementById } from "@scripts/utils"

const callApp = new CallApp({
  target: getElementById(`svelte`),
})

export default callApp
