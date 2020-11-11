from allauth.account.models import EmailAddress as EmailAddress
from allauth.socialaccount.providers.base import ProviderAccount as ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider as OAuth2Provider
from typing import Any

class NaverAccount(ProviderAccount):
    def get_avatar_url(self): ...
    def to_str(self): ...

class NaverProvider(OAuth2Provider):
    id: str = ...
    name: str = ...
    account_class: Any = ...
    def extract_uid(self, data: Any): ...
    def extract_common_fields(self, data: Any): ...
    def extract_email_addresses(self, data: Any): ...

provider_classes: Any
