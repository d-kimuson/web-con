from allauth.socialaccount.providers.base import ProviderAccount as ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider as OAuth2Provider
from typing import Any

class ShareFileAccount(ProviderAccount):
    def to_str(self): ...

class ShareFileProvider(OAuth2Provider):
    id: str = ...
    name: str = ...
    account_class: Any = ...
    def extract_uid(self, data: Any): ...
    def extract_common_fields(self, data: Any): ...

provider_classes: Any
