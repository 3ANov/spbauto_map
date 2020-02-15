from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView
from django.shortcuts import render

# Create your views here.
from django_registration.backends.one_step.views import RegistrationView
from sitesettings.models import SiteSettings


class LoginViewCustom(LoginView):
    template_name = 'accounts/login.html'
    sitesettings = SiteSettings.load()
    extra_context = {'sitesettings': sitesettings}


class LogoutViewCustom(LogoutView):
    template_name = 'accounts/logout.html'
    sitesettings = SiteSettings.load()
    extra_context = {'sitesettings': sitesettings}


class PasswordResetViewCustom(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    html_email_template_name = 'accounts/password_reset_email.html'
    sitesettings = SiteSettings.load()
    extra_context = {'sitesettings': sitesettings}


class PasswordResetConfirmViewCustom(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    sitesettings = SiteSettings.load()
    extra_context = {'sitesettings': sitesettings}


class PasswordResetDoneViewCustom(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'
    sitesettings = SiteSettings.load()
    extra_context = {'sitesettings': sitesettings}


class RegistrationViewCustom(RegistrationView):
    template_name = 'accounts/registration_form.html'
    sitesettings = SiteSettings.load()
    extra_context = {'sitesettings': sitesettings}