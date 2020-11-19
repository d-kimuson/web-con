// DOM
interface HTMLVideoElement {
  playsInline?: boolean
}

// Application
interface User {
  name: string
  userId: string
}

// API
interface UserSerializer {
  pk: string
  email: string
}

interface TagSerializer {
  pk: string
  name: string
}

interface RoomUserSerializer {
  pk: string
  user: UserSerializer
}

interface RoomSerializer {
  pk: string
  title: string
  description: string
  start_datetime: string
  end_datetime: string
  is_possible_join: string
  room_members: RoomUserSerializer[]
  tags: TagSerializer[]
}
