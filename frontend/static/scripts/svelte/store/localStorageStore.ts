import { get, writable as internal, Writable } from "svelte/store"

type Storeable = string | number | boolean

export class LocalStorageStore<T extends Storeable> implements Writable<T> {
  private store: Writable<T>
  public subscribe

  constructor(private key: string, defaultValue: T) {
    const stored = localStorage.getItem(key)

    this.store = internal(stored ? this.toT(stored) : defaultValue)
    this.subscribe = this.store.subscribe
  }

  get(): T {
    return get(this.store)
  }

  set(value: T): void {
    this.store.set(value)
    this.setLocalStorage(value)
  }

  update(f: (arg0: T) => T): void {
    const value = f(this.get())
    this.set(value)
  }

  // Store
  setStore(value: T): void {
    this.store.set(value)
  }

  getStore(): T {
    return get(this.store)
  }

  // LocalStorage
  getLocalStorage(): Promise<T | undefined> {
    const stringValue = localStorage.getItem(this.key)
    return stringValue ? JSON.parse(stringValue) : undefined
  }

  setLocalStorage(value: T): void {
    const stringValue = JSON.stringify(value)
    localStorage.setItem(this.key, stringValue)
  }

  // Convert
  toString(value: T): string {
    return JSON.stringify(value)
  }

  toT(stringValue: string): T {
    return JSON.parse(stringValue)
  }
}
