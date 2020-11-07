from .provider import DwollaProvider as DwollaProvider
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter as OAuth2Adapter, OAuth2CallbackView as OAuth2CallbackView, OAuth2LoginView as OAuth2LoginView
from typing import Any

ENVIRONMENTS: Any
ENV: Any
AUTH_URL: Any
TOKEN_URL: Any

class DwollaOAuth2Adapter(OAuth2Adapter):
    scope_delimiter: str = ...
    provider_id: Any = ...
    access_token_url: Any = ...
    authorize_url: Any = ...
    def complete_login(self, request: Any, app: Any, token: Any, response: Any, **kwargs: Any): ...

oauth2_login: Any
oauth2_callback: Any
