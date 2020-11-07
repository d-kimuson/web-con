from . import app_settings as app_settings, signals as signals
from ..exceptions import ImmediateHttpResponse as ImmediateHttpResponse
from ..utils import get_form_class as get_form_class, get_request_param as get_request_param
from .adapter import get_adapter as get_adapter
from .forms import AddEmailForm as AddEmailForm, ChangePasswordForm as ChangePasswordForm, LoginForm as LoginForm, ResetPasswordForm as ResetPasswordForm, ResetPasswordKeyForm as ResetPasswordKeyForm, SetPasswordForm as SetPasswordForm, SignupForm as SignupForm, UserTokenForm as UserTokenForm
from .models import EmailAddress as EmailAddress, EmailConfirmation as EmailConfirmation, EmailConfirmationHMAC as EmailConfirmationHMAC
from .utils import complete_signup as complete_signup, get_login_redirect_url as get_login_redirect_url, get_next_redirect_url as get_next_redirect_url, logout_on_password_change as logout_on_password_change, passthrough_next_redirect_url as passthrough_next_redirect_url, perform_login as perform_login, sync_user_email_addresses as sync_user_email_addresses, url_str_to_user_pk as url_str_to_user_pk
from django.views.generic.base import TemplateResponseMixin, TemplateView, View
from django.views.generic.edit import FormView
from typing import Any, Optional

INTERNAL_RESET_URL_KEY: str
INTERNAL_RESET_SESSION_KEY: str
sensitive_post_parameters_m: Any

class RedirectAuthenticatedUserMixin:
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...
    def get_authenticated_redirect_url(self): ...

class AjaxCapableProcessFormViewMixin:
    def get(self, request: Any, *args: Any, **kwargs: Any): ...
    def post(self, request: Any, *args: Any, **kwargs: Any): ...
    def get_form(self, form_class: Optional[Any] = ...): ...
    def get_ajax_data(self) -> None: ...

class LogoutFunctionalityMixin:
    def logout(self) -> None: ...

class LoginView(RedirectAuthenticatedUserMixin, AjaxCapableProcessFormViewMixin, FormView):
    form_class: Any = ...
    template_name: Any = ...
    success_url: Any = ...
    redirect_field_name: str = ...
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...
    def get_form_kwargs(self): ...
    def get_form_class(self): ...
    def form_valid(self, form: Any): ...
    def get_success_url(self): ...
    def get_context_data(self, **kwargs: Any): ...

login: Any

class CloseableSignupMixin:
    template_name_signup_closed: Any = ...
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...
    def is_open(self): ...
    def closed(self): ...

class SignupView(RedirectAuthenticatedUserMixin, CloseableSignupMixin, AjaxCapableProcessFormViewMixin, FormView):
    template_name: Any = ...
    form_class: Any = ...
    redirect_field_name: str = ...
    success_url: Any = ...
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...
    def get_form_class(self): ...
    def get_success_url(self): ...
    user: Any = ...
    def form_valid(self, form: Any): ...
    def get_context_data(self, **kwargs: Any): ...

signup: Any

class ConfirmEmailView(TemplateResponseMixin, LogoutFunctionalityMixin, View):
    template_name: Any = ...
    object: Any = ...
    def get(self, *args: Any, **kwargs: Any): ...
    def post(self, *args: Any, **kwargs: Any): ...
    def login_on_confirm(self, confirmation: Any): ...
    def get_object(self, queryset: Optional[Any] = ...): ...
    def get_queryset(self): ...
    def get_context_data(self, **kwargs: Any): ...
    def get_redirect_url(self): ...

confirm_email: Any

class EmailView(AjaxCapableProcessFormViewMixin, FormView):
    template_name: Any = ...
    form_class: Any = ...
    success_url: Any = ...
    def get_form_class(self): ...
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...
    def get_form_kwargs(self): ...
    def form_valid(self, form: Any): ...
    def post(self, request: Any, *args: Any, **kwargs: Any): ...
    def get_context_data(self, **kwargs: Any): ...
    def get_ajax_data(self): ...

email: Any

class PasswordChangeView(AjaxCapableProcessFormViewMixin, FormView):
    template_name: Any = ...
    form_class: Any = ...
    success_url: Any = ...
    def get_form_class(self): ...
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...
    def render_to_response(self, context: Any, **response_kwargs: Any): ...
    def get_form_kwargs(self): ...
    def form_valid(self, form: Any): ...
    def get_context_data(self, **kwargs: Any): ...

password_change: Any

class PasswordSetView(AjaxCapableProcessFormViewMixin, FormView):
    template_name: Any = ...
    form_class: Any = ...
    success_url: Any = ...
    def get_form_class(self): ...
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...
    def render_to_response(self, context: Any, **response_kwargs: Any): ...
    def get_form_kwargs(self): ...
    def form_valid(self, form: Any): ...
    def get_context_data(self, **kwargs: Any): ...

password_set: Any

class PasswordResetView(AjaxCapableProcessFormViewMixin, FormView):
    template_name: Any = ...
    form_class: Any = ...
    success_url: Any = ...
    redirect_field_name: str = ...
    def get_form_class(self): ...
    def form_valid(self, form: Any): ...
    def get_context_data(self, **kwargs: Any): ...

password_reset: Any

class PasswordResetDoneView(TemplateView):
    template_name: Any = ...

password_reset_done: Any

class PasswordResetFromKeyView(AjaxCapableProcessFormViewMixin, LogoutFunctionalityMixin, FormView):
    template_name: Any = ...
    form_class: Any = ...
    success_url: Any = ...
    def get_form_class(self): ...
    request: Any = ...
    key: Any = ...
    reset_user: Any = ...
    def dispatch(self, request: Any, uidb36: Any, key: Any, **kwargs: Any): ...
    def get_context_data(self, **kwargs: Any): ...
    def get_form_kwargs(self): ...
    def form_valid(self, form: Any): ...

password_reset_from_key: Any

class PasswordResetFromKeyDoneView(TemplateView):
    template_name: Any = ...

password_reset_from_key_done: Any

class LogoutView(TemplateResponseMixin, LogoutFunctionalityMixin, View):
    template_name: Any = ...
    redirect_field_name: str = ...
    def get(self, *args: Any, **kwargs: Any): ...
    def post(self, *args: Any, **kwargs: Any): ...
    def get_context_data(self, **kwargs: Any): ...
    def get_redirect_url(self): ...

logout: Any

class AccountInactiveView(TemplateView):
    template_name: Any = ...

account_inactive: Any

class EmailVerificationSentView(TemplateView):
    template_name: Any = ...

email_verification_sent: Any
