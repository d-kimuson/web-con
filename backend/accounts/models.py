from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.utils import timezone
import uuid
from typing import List


class UserManager(BaseUserManager):
    def _create_user(self, email: str, password: str, is_staff: bool, is_superuser: bool) -> 'User':
        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=timezone.now(),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str) -> 'User':
        return self._create_user(email, password, False, False)

    def create_superuser(self, email: str, password: str) -> 'User':
        return self._create_user(email, password, True, True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(
        _('password'),
        max_length=128,
        validators=[MinLengthValidator(5)]
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: List[str] = []

    objects = UserManager()

    def __repr__(self) -> str:
        return "User <{}>".format(self.email)

    __str__ = __repr__
