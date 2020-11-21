import pytest
from django.utils import timezone
from datetime import datetime, timedelta

from django.conf import settings
from accounts.tests.test_models import basic_user, basic_user2, basic_user3
from accounts.models import User
from ..models import Room, Tag, RoomTag, RoomUser

now = timezone.now()


# =================
# Room
# =================
@pytest.fixture
def room_大学生集合_募集中(basic_user: User):
    return Room.objects.create(
        title="大学生集合",
        description="大学生で雑談しましょう！",
        created_by=basic_user,
        start_datetime=now + timedelta(hours=10),
        end_datetime=now + timedelta(hours=11),
        is_possible_join=True
    )


@pytest.fixture
def room_高校生集合_締切(basic_user: User):
    return Room.objects.create(
        title="高校生集合",
        description="高校生で雑談しましょう！",
        created_by=basic_user,
        start_datetime=now + timedelta(hours=10),
        end_datetime=now + timedelta(hours=11),
        is_possible_join=False
    )


@pytest.fixture
def room_中学生集合_開催中(basic_user2: User):
    return Room.objects.create(
        title="中学生集合",
        description="中学生で雑談しましょう！",
        created_by=basic_user2,
        start_datetime=now - timedelta(hours=1),
        end_datetime=now + timedelta(hours=1),
        is_possible_join=True
    )


# =================
# タグ
# =================
@pytest.fixture
def tag_大学生():
    return Tag.objects.create(
        name="大学生"
    )


@pytest.fixture
def tag_高校生():
    return Tag.objects.create(
        name="高学生"
    )

# =================
# ルームタグ
# =================


@pytest.fixture
def roomtag_大学生集合_大学生(room_大学生集合_募集中: Room, tag_大学生: Tag):
    return RoomTag.objects.create(
        room=room_大学生集合_募集中,
        tag=tag_大学生
    )


# =================
# ルームユーザー
# =================
@pytest.fixture
def roomuser_大学生集合_basic_user(basic_user: User, room_大学生集合_募集中: Room):
    return RoomUser.objects.create(
        user=basic_user,
        room=room_大学生集合_募集中,
    )


@pytest.fixture
def roomuser_大学生集合_basic_user2(basic_user2: User, room_大学生集合_募集中: Room):
    return RoomUser.objects.create(
        user=basic_user2,
        room=room_大学生集合_募集中,
    )


@pytest.fixture
def roomuser_中学生集合_basic_user(basic_user: User, room_中学生集合_開催中: Room):
    return RoomUser.objects.create(
        user=basic_user,
        room=room_中学生集合_開催中,
    )


@pytest.fixture
def roomuser_中学生集合_basic_user2(basic_user2: User, room_中学生集合_開催中: Room):
    return RoomUser.objects.create(
        user=basic_user2,
        room=room_中学生集合_開催中,
    )

# =================
# テスト
# =================


@pytest.mark.django_db
class T_RoomIsOpen:
    pytestmark = pytest.mark.django_db

    def case_予定部屋(self, room_大学生集合_募集中):
        assert room_大学生集合_募集中.is_open == False

    def case_開催中部屋(self, room_中学生集合_開催中):
        assert room_中学生集合_開催中.is_open == True


@pytest.mark.django_db
class T_RoomMembers:
    pytestmark = pytest.mark.django_db

    def case_通常(
        self,
        basic_user, basic_user2,
        room_大学生集合_募集中,
        roomuser_大学生集合_basic_user,
    ):
        assert room_大学生集合_募集中.members.filter(pk=basic_user.pk).exists() == True
        assert room_大学生集合_募集中.members.filter(pk=basic_user2.pk).exists() == False


@pytest.mark.django_db
class T_RoomTags:
    pytestmark = pytest.mark.django_db

    def case_通常(
        self,
        tag_大学生,
        tag_高校生,
        room_大学生集合_募集中,
        roomtag_大学生集合_大学生,
    ):
        assert room_大学生集合_募集中.tags.filter(pk=tag_大学生.pk).exists() == True
        assert room_大学生集合_募集中.tags.filter(pk=tag_高校生.pk).exists() == False


@pytest.mark.django_db
class T_RoomCheckPermission:
    pytestmark = pytest.mark.django_db

    def case_未参加ユーザー_開催なし(
        self,
        basic_user2,
        room_大学生集合_募集中,
        roomuser_大学生集合_basic_user,
    ):
        assert room_大学生集合_募集中.check_permission(basic_user2) == False

    def case_参加ユーザー_開催なし(
        self,
        basic_user2,
        room_大学生集合_募集中,
        roomuser_大学生集合_basic_user,
        roomuser_大学生集合_basic_user2,
    ):
        assert room_大学生集合_募集中.check_permission(basic_user2) == False

    def case_未参加ユーザー_開催中(
        self,
        basic_user2,
        room_中学生集合_開催中,
        roomuser_中学生集合_basic_user,
    ):
        assert room_中学生集合_開催中.check_permission(basic_user2) == False

    def case_参加ユーザー_開催中(
        self,
        basic_user2,
        room_中学生集合_開催中,
        roomuser_中学生集合_basic_user,
        roomuser_中学生集合_basic_user2,
    ):
        assert room_中学生集合_開催中.check_permission(basic_user2) == True
