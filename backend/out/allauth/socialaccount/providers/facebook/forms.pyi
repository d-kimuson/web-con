from django import forms
from typing import Any

class FacebookConnectForm(forms.Form):
    access_token: Any = ...
