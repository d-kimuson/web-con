import axios from "axios"

import { ApiApiFactory as getEndpoints, Configuration } from "../openapi"

export const api = axios.create({
  baseURL: `/api/`,
  timeout: 1000,
  withCredentials: true,
  xsrfCookieName: `csrftoken`,
  xsrfHeaderName: `X-CSRFTOKEN`,
})

const config = new Configuration()
export const endpoints = getEndpoints(config, `http://localhost:3000`, api)

// openapi を使うようになったので、削除予定です
// 一応しばらくの間だけ残しておきます

// interface Response<T> {
//   status: number
//   data: T
// }

// LOGIN User Info
// export const loginUser = async (): Promise<UserSerializer | undefined> => {
//   try {
//     const response: Response<UserSerializer> = await api.get(
//       `/users/login_user/`,
//     )

//     return response.data
//   } catch (error) {
//     const { status, statusText } = error.response

//     console.log(`ERROR(${status}): ${statusText}`)
//   }
// }

// 部屋一覧
// export const roomList = async (): Promise<RoomSerializer[] | undefined> => {
//   try {
//     const response: Response<RoomSerializer[]> = await api.get(`/rooms/`)

//     return response.data
//   } catch (error) {
//     const { status, statusText } = error.response

//     console.log(`ERROR(${status}): ${statusText}`)
//   }
// }

// 個別部屋情報
// type RoomDetailResponse = Omit<
//   RoomSerializer,
//   "start_datetime" | "end_datetime"
// > & {
//   start_datetime: Dayjs
//   end_datetime: Dayjs
// }

// export const roomDetail = async (
//   roomId: string,
// ): Promise<RoomDetailResponse | undefined> => {
//   try {
//     const response: Response<RoomSerializer> = await api.get(
//       `/rooms/${roomId}/`,
//     )
//     const tmp = {
//       ...response.data,
//       start_datetime: dayjs(response.data.start_datetime),
//       end_datetime: dayjs(response.data.end_datetime),
//     }

//     return tmp
//   } catch (error) {
//     const { status, statusText } = error.response

//     console.log(`ERROR(${status}): ${statusText}`)
//   }
// }

// 使わなくなったので削除予定です
// interface JoinRoomResponse {
//   message: string
//   user: UserSerializer
//   room: RoomSerializer
// }
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
