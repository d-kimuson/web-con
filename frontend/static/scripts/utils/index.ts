export const getElementById = (id: string): HTMLElement => {
  // null でない要素を id から取得する関数
  // 存在してない id に対しては例外をなげる
  const elm = document.getElementById(id)

  if (elm !== null) {
    return elm
  } else {
    throw new Error(`HTMLElemet: id=${id}が存在しません`)
  }
}
