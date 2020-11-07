from allauth.socialaccount import app_settings as app_settings
from allauth.socialaccount.providers.github.provider import GitHubProvider as GitHubProvider
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter as OAuth2Adapter, OAuth2CallbackView as OAuth2CallbackView, OAuth2LoginView as OAuth2LoginView
from typing import Any

class GitHubOAuth2Adapter(OAuth2Adapter):
    provider_id: Any = ...
    settings: Any = ...
    web_url: Any = ...
    api_url: Any = ...
    access_token_url: Any = ...
    authorize_url: Any = ...
    profile_url: Any = ...
    emails_url: Any = ...
    def complete_login(self, request: Any, app: Any, token: Any, **kwargs: Any): ...
    def get_email(self, headers: Any): ...

oauth2_login: Any
oauth2_callback: Any
