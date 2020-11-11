from allauth.socialaccount.providers.base import ProviderAccount as ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider as OAuth2Provider
from typing import Any

class StackExchangeAccount(ProviderAccount):
    def get_profile_url(self): ...
    def get_avatar_url(self): ...
    def to_str(self): ...

class StackExchangeProvider(OAuth2Provider):
    id: str = ...
    name: str = ...
    account_class: Any = ...
    def get_site(self): ...
    def extract_uid(self, data: Any): ...
    def extract_common_fields(self, data: Any): ...

provider_classes: Any
