from .provider import CoinbaseProvider as CoinbaseProvider
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter as OAuth2Adapter, OAuth2CallbackView as OAuth2CallbackView, OAuth2LoginView as OAuth2LoginView
from typing import Any

class CoinbaseOAuth2Adapter(OAuth2Adapter):
    provider_id: Any = ...
    @property
    def authorize_url(self): ...
    @property
    def access_token_url(self): ...
    @property
    def profile_url(self): ...
    def complete_login(self, request: Any, app: Any, token: Any, **kwargs: Any): ...

oauth2_login: Any
oauth2_callback: Any
