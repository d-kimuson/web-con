import axios from "axios"

export const api = axios.create({
  baseURL: `/api/`,
  timeout: 1000,
  withCredentials: true,
  xsrfCookieName: `csrftoken`,
  xsrfHeaderName: `X-CSRFTOKEN`,
})

// API Endpoint Definition
interface JoinRoomResponse {
  message: string
  user: UserSerializer
  room: RoomSerializer
}

export const loginUser = async (): Promise<UserSerializer | undefined> => {
  try {
    const response: {
      status: number
      data: UserSerializer
    } = await api.get(`/users/login_user/`)

    return response.data
  } catch (error) {
    const { status, statusText } = error.response

    console.log(`ERROR(${status}): ${statusText}`)
  }
}

// 使わなくなったので削除予定です
// export const joinRoom = async (
//   roomId: string,
//   peerId: string,
// ): Promise<JoinRoomResponse | undefined> => {
//   try {
//     const response: {
//       status: number
//       data: JoinRoomResponse
//     } = await api.post(`/rooms/${roomId}/join/`, {
//       peerId,
//     })

//     return response.data
//   } catch (error) {
//     const { status, statusText } = error.response

//     console.log(`ERROR(${status}): ${statusText}`)
//   }
// }

export const roomList = async (): Promise<RoomSerializer[] | undefined> => {
  try {
    const response: RoomSerializer[] = await api.get(`/rooms/`)

    return response
  } catch (error) {
    const { status, statusText } = error.response

    console.log(`ERROR(${status}): ${statusText}`)
  }
}

export const roomDetail = async (
  roomId: string,
): Promise<RoomSerializer | undefined> => {
  try {
    const response: RoomSerializer = await api.get(`/rooms/${roomId}/`)

    return response
  } catch (error) {
    const { status, statusText } = error.response

    console.log(`ERROR(${status}): ${statusText}`)
  }
}
