from .provider import UntappdProvider as UntappdProvider
from allauth.socialaccount import app_settings as app_settings
from allauth.socialaccount.providers.oauth2.client import OAuth2Client as OAuth2Client, OAuth2Error as OAuth2Error
from typing import Any

class UntappdOAuth2Client(OAuth2Client):
    def get_access_token(self, code: Any): ...
