from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from django.utils import timezone
from datetime import datetime
import uuid
from typing import Union

from accounts.models import User


class Room(models.Model):
    """
    仮実装、とりあえず通話参加用にIDとタイトルだけ持ったモデルを用意しておく

    他に募集中(or確定済み)、関連タグ、参加ユーザー、開始時間&終了時間、等の情報も必要になるはず
    """
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    title = models.CharField(max_length=127)
    description = models.TextField(default='')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room_created')
    start_datetime = models.DateTimeField(verbose_name='開始時間')
    end_datetime = models.DateTimeField(verbose_name='終了時間')
    is_possible_join = models.BooleanField(default=True, verbose_name='募集中')

    def check_permission(self, user: Union[AbstractBaseUser, AnonymousUser]) -> bool:
        """ユーザーに対してアクセス権があるかを確認する関数

        Args:
            user (User): 部屋に入るユーザー

        Returns:
            bool: 権限の有無
        """
        return self._check_permission(user, timezone.now())

    def _check_permission(self, user: Union[AbstractBaseUser, AnonymousUser], now: datetime) -> bool:
        # 仮実装で全部True
        # 実際は部屋の属性とアクセスユーザー情報を比較して権限の有無を確認する
        return True

    def __repr__(self) -> str:
        return "Room <{}>".format(self.title)

    __str__ = __repr__


class Tag(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    name = models.CharField(
        max_length=127,
        unique=True)

    def __repr__(self) -> str:
        return "Tag <{}>".format(self.name)

    __str__ = __repr__


class RoomTag(models.Model):
    class Meta:
        unique_together = (
            ('room', 'tag',)
        )

    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='roomtag',
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
    )

    def __repr__(self) -> str:
        return "RoomTag <{}, {}>".format(self.room.title, self.tag.name)

    __str__ = __repr__


class RoomUser(models.Model):
    class Meta:
        unique_together = (
            ('user', 'room',),
        )

    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # userの削除をどうするか
        related_name='roomuser',
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='roomuser',
    )
