from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include
from django.views.generic import TemplateView
from django_registration.backends.activation.views import RegistrationView, ActivationView

from accounts.forms import CustomUserCreationForm

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('register/', RegistrationView.as_view(success_url='/', form_class=CustomUserCreationForm,
                                               template_name='registration/registration_form.html',
                                               email_body_template='registration/activation_email.txt',
                                               email_subject_template='registration/activation_email_subject.txt'),
         name='django_registration_register'),
    path('activate/complete/',
            TemplateView.as_view(
                template_name="registration/activation_complete.html"
            ),
            name="django_registration_activation_complete",
        ),

    path('activate/<str:activation_key>/',
         ActivationView.as_view(template_name='registration/activation_failed.html'),
         name="django_registration_activate"),

    path('', include('social_django.urls', namespace='social'))
]
