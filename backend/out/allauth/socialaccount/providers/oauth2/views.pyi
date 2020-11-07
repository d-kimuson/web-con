from ..base import AuthAction as AuthAction, AuthError as AuthError
from allauth.exceptions import ImmediateHttpResponse as ImmediateHttpResponse
from allauth.socialaccount import providers as providers
from allauth.socialaccount.helpers import complete_social_login as complete_social_login, render_authentication_error as render_authentication_error
from allauth.socialaccount.models import SocialLogin as SocialLogin, SocialToken as SocialToken
from allauth.socialaccount.providers.base import ProviderException as ProviderException
from allauth.socialaccount.providers.oauth2.client import OAuth2Client as OAuth2Client, OAuth2Error as OAuth2Error
from allauth.utils import build_absolute_uri as build_absolute_uri, get_request_param as get_request_param
from typing import Any

class OAuth2Adapter:
    expires_in_key: str = ...
    client_class: Any = ...
    supports_state: bool = ...
    redirect_uri_protocol: Any = ...
    access_token_method: str = ...
    login_cancelled_error: str = ...
    scope_delimiter: str = ...
    basic_auth: bool = ...
    headers: Any = ...
    request: Any = ...
    def __init__(self, request: Any) -> None: ...
    def get_provider(self): ...
    def complete_login(self, request: Any, app: Any, access_token: Any, **kwargs: Any) -> None: ...
    def get_callback_url(self, request: Any, app: Any): ...
    def parse_token(self, data: Any): ...
    def get_access_token_data(self, request: Any, app: Any, client: Any): ...

class OAuth2View:
    request: Any = ...
    adapter: Any = ...
    @classmethod
    def adapter_view(cls, adapter: Any): ...
    def get_client(self, request: Any, app: Any): ...

class OAuth2LoginView(OAuth2View):
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...

class OAuth2CallbackView(OAuth2View):
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...
