import pytest

from ..models import User


@pytest.fixture
def basic_user():
    return User.objects.create_user(
        email='user@example.com',
        password='password'
    )


@pytest.fixture
def admin_user():
    return User.objects.create_superuser(
        email='admin@example.com',
        password='password'
    )


@pytest.mark.django_db
class T_ユーザー作成:
    pytestmark = pytest.mark.django_db

    def case_基本(self):
        email = 'user@example.com'
        password = 'password'
        user = User.objects._create_user(
            email=email,
            password=password,
            is_staff=False,
            is_superuser=False
        )
        assert isinstance(user, User)
        assert user.email == email
        assert user.password != password  # ハッシュ化のチェック
        assert user.is_staff == False
        assert user.is_superuser == False

    def case_create_user(self):
        email = 'user@example.com'
        password = 'password'
        user = User.objects.create_user(
            email=email,
            password=password,
        )
        assert user.is_staff == False
        assert user.is_superuser == False

    def case_create_superuser(self):
        email = 'user@example.com'
        password = 'password'
        user = User.objects.create_superuser(
            email=email,
            password=password,
        )
        assert user.is_staff == True
        assert user.is_superuser == True


@pytest.mark.django_db
class T_ユーザー認証:
    pytestmark = pytest.mark.django_db

    def case_基本(self, basic_user):
        assert basic_user.check_password('password') == True

    def case_失敗(self, basic_user):
        assert basic_user.check_password('missed_password') == False
