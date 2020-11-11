from allauth.account.models import EmailAddress as EmailAddress
from allauth.account.utils import user_email as user_email
from allauth.utils import get_user_model as get_user_model
from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None: ...
    def get_users_with_multiple_primary_email(self): ...
    def unprimary_extra_primary_emails(self, user: Any) -> None: ...
