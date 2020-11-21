import { LocalStorageStore } from "./localStorageStore"

export const isVideoOnStore = new LocalStorageStore<boolean>(`isVideoOn`, false)
export const isMuteStore = new LocalStorageStore<boolean>(`isMute`, false)
