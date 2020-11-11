from .models import EmailAddress as EmailAddress
from .utils import send_email_confirmation as send_email_confirmation
from typing import Any, Optional

def verified_email_required(function: Optional[Any] = ..., login_url: Optional[Any] = ..., redirect_field_name: Any = ...): ...
