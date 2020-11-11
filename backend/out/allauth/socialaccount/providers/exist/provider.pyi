from allauth.socialaccount.providers.base import ProviderAccount as ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider as OAuth2Provider
from typing import Any

class ExistAccount(ProviderAccount):
    def get_profile_url(self): ...
    def get_avatar_url(self): ...
    def to_str(self): ...

class ExistProvider(OAuth2Provider):
    id: str = ...
    name: str = ...
    account_class: Any = ...
    def extract_uid(self, data: Any): ...
    def extract_common_fields(self, data: Any): ...
    def get_default_scope(self): ...

provider_classes: Any
