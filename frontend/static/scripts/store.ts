import { LocalStorageStore } from "./localStorageStore"

export const isVideoOn = new LocalStorageStore<boolean>(`isVideoOn`, false)
export const isMute = new LocalStorageStore<boolean>(`isMute`, false)
