from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetCompleteView

# Create your views here.
from django_registration.backends.one_step.views import RegistrationView
from site_settings.models import SiteSettings


class LoginViewCustom(LoginView):
    template_name = 'accounts/templates/accounts/login.html'
    sitesettings = SiteSettings.load()
    extra_context = {'site_settings': sitesettings}


class LogoutViewCustom(LogoutView):
    template_name = 'accounts/templates/accounts/logout.html'
    sitesettings = SiteSettings.load()
    extra_context = {'site_settings': sitesettings}


class PasswordResetViewCustom(PasswordResetView):
    template_name = 'accounts/templates/accounts/password_reset_form.html'
    html_email_template_name = 'accounts/password_reset_email.html'
    sitesettings = SiteSettings.load()
    extra_context = {'site_settings': sitesettings}


class PasswordResetConfirmViewCustom(PasswordResetConfirmView):
    template_name = 'accounts/templates/accounts/password_reset_confirm.html'
    sitesettings = SiteSettings.load()
    extra_context = {'site_settings': sitesettings}


class PasswordResetDoneViewCustom(PasswordResetDoneView):
    template_name = 'accounts/templates/accounts/password_reset_done.html'
    sitesettings = SiteSettings.load()
    extra_context = {'site_settings': sitesettings}


class PasswordResetCompleteViewCustom(PasswordResetCompleteView):
    template_name = 'accounts/templates/accounts/password_reset_complete.html'
    sitesettings = SiteSettings.load()
    extra_context = {'site_settings': sitesettings}


class RegistrationViewCustom(RegistrationView):
    template_name = 'accounts/templates/accounts/registration_form.html'
    sitesettings = SiteSettings.load()
    extra_context = {'site_settings': sitesettings}