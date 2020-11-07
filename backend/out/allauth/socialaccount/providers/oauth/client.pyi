from allauth.utils import build_absolute_uri as build_absolute_uri, get_request_param as get_request_param
from typing import Any, Optional

def get_token_prefix(url: Any): ...

class OAuthError(Exception): ...

class OAuthClient:
    request: Any = ...
    request_token_url: Any = ...
    access_token_url: Any = ...
    consumer_key: Any = ...
    consumer_secret: Any = ...
    parameters: Any = ...
    callback_url: Any = ...
    provider: Any = ...
    errors: Any = ...
    request_token: Any = ...
    access_token: Any = ...
    def __init__(self, request: Any, consumer_key: Any, consumer_secret: Any, request_token_url: Any, access_token_url: Any, callback_url: Any, parameters: Optional[Any] = ..., provider: Optional[Any] = ...) -> None: ...
    def get_access_token(self): ...
    def is_valid(self): ...
    def get_redirect(self, authorization_url: Any, extra_params: Any): ...

class OAuth:
    request: Any = ...
    consumer_key: Any = ...
    secret_key: Any = ...
    request_token_url: Any = ...
    def __init__(self, request: Any, consumer_key: Any, secret_key: Any, request_token_url: Any) -> None: ...
    def query(self, url: Any, method: str = ..., params: Optional[Any] = ..., headers: Optional[Any] = ...): ...
