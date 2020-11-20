from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from typing import Any, Dict

from accounts.serializers import UserSerializer
from .models import Room, Tag, RoomUser


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('pk', 'name',)


class RoomUserSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = RoomUser
        fields = ('pk', 'user',)

    @extend_schema_field(UserSerializer)
    def get_user(self, obj: RoomUser) -> Dict[str, Any]:
        return UserSerializer(instance=obj.user).data


class RoomSerializer(serializers.ModelSerializer):
    room_members = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ('pk', 'title', 'description', 'start_datetime',
                  'end_datetime', 'is_possible_join', 'room_members', 'tags',)

    @extend_schema_field(RoomUserSerializer(many=True))
    def get_room_members(self, obj: Room) -> Dict[str, Any]:
        return RoomUserSerializer(instance=RoomUser.objects.filter(room=obj), many=True).data

    @extend_schema_field(TagSerializer(many=True))
    def get_tags(self, obj: Room) -> Dict[str, Any]:
        return TagSerializer(instance=obj.tags, many=True).data
