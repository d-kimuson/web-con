from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework .response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from typing import Dict, Any, Optional

from accounts.models import User
from accounts.serializers import UserSerializer
from .models import Room
from .serializers import RoomSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['GET'], detail=False, url_path='login_user', permission_classes=(IsAuthenticated,))
    def login_user(self, request: Request) -> Response:
        return Response(
            self.get_serializer(instance=self.request.user).data
        )


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @action(methods=['POST'], detail=True, url_path='join', permission_classes=(IsAuthenticated,))
    def join(self, request: Request, pk: Optional[str] = None, **kwargs: Dict[str, Any]) -> Response:
        user = request.user
        room = self.get_object()
        peer_id = request.data.get('peerId', None)

        if not isinstance(user, User) or not isinstance(peer_id, str) or not isinstance(room, Room):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if not room.check_permission(user):
            return Response(status=status.HTTP_403_FORBIDDEN)

        room_user = room.roomuser.get(user=user)
        room_user.peer_id = peer_id
        room_user.save()

        return Response(status=status.HTTP_200_OK, data={
            'message': 'peerIDが登録されました',
            'room': RoomSerializer(instance=room, many=False).data,
            'user': UserSerializer(instance=user, many=False).data,
        })
