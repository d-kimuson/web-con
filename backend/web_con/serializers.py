from rest_framework import serializers
from typing import Any, Dict

from accounts.serializers import UserSerializer
from .models import Room, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('pk', 'name',)


class RoomSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ('pk', 'title', 'description', 'start_datetime',
                  'end_datetime', 'is_possible_join', 'members', 'tags',)

    def get_members(self, obj: Room) -> Dict[str, Any]:
        return UserSerializer(instance=obj.members, many=True).data

    def get_tags(self, obj: Room) -> Dict[str, Any]:
        return TagSerializer(instance=obj.tags, many=True).data
