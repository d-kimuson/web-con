from .provider import ShopifyProvider as ShopifyProvider
from allauth.exceptions import ImmediateHttpResponse as ImmediateHttpResponse
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter as OAuth2Adapter, OAuth2CallbackView as OAuth2CallbackView, OAuth2LoginView as OAuth2LoginView
from typing import Any

class ShopifyOAuth2Adapter(OAuth2Adapter):
    provider_id: Any = ...
    supports_state: bool = ...
    scope_delimiter: str = ...
    @property
    def access_token_url(self): ...
    @property
    def authorize_url(self): ...
    @property
    def profile_url(self): ...
    def complete_login(self, request: Any, app: Any, token: Any, **kwargs: Any): ...

class ShopifyOAuth2LoginView(OAuth2LoginView):
    def dispatch(self, request: Any): ...

oauth2_login: Any
oauth2_callback: Any
