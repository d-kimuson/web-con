from allauth.socialaccount.providers.base import ProviderAccount as ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider as OAuth2Provider
from typing import Any

class MailChimpAccount(ProviderAccount):
    def get_profile_url(self): ...
    def get_avatar_url(self): ...

class MailChimpProvider(OAuth2Provider):
    id: str = ...
    name: str = ...
    account_class: Any = ...
    def extract_uid(self, data: Any): ...
    def get_default_scope(self): ...
    def extract_common_fields(self, data: Any): ...

provider_classes: Any
