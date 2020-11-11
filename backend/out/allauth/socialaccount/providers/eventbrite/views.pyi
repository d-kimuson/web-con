from .provider import EventbriteProvider as EventbriteProvider
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter as OAuth2Adapter, OAuth2CallbackView as OAuth2CallbackView, OAuth2LoginView as OAuth2LoginView
from typing import Any

class EventbriteOAuth2Adapter(OAuth2Adapter):
    provider_id: Any = ...
    authorize_url: str = ...
    access_token_url: str = ...
    profile_url: str = ...
    def complete_login(self, request: Any, app: Any, token: Any, **kwargs: Any): ...

oauth2_login: Any
oauth2_callback: Any
