from .provider import SteamOpenIDProvider as SteamOpenIDProvider
from allauth.socialaccount.providers.openid.views import OpenIDCallbackView as OpenIDCallbackView, OpenIDLoginView as OpenIDLoginView
from typing import Any

STEAM_OPENID_URL: str

class SteamOpenIDLoginView(OpenIDLoginView):
    provider: Any = ...
    def get_form(self): ...
    def get_callback_url(self): ...

class SteamOpenIDCallbackView(OpenIDCallbackView):
    provider: Any = ...

steam_login: Any
steam_callback: Any
