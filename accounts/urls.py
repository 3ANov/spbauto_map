from django.shortcuts import redirect
from django.urls import path
from . import views
from .views import RegistrationViewCustom
from .signals import *

urlpatterns = [
    path('login/', views.LoginViewCustom.as_view(), name='login'),
    path('logout/', views.LogoutViewCustom.as_view(), name='logout'),
    path('password-reset/', views.PasswordResetViewCustom.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneViewCustom.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmViewCustom.as_view(), name='password_reset_confirm'),
    #path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('register/',
         RegistrationViewCustom.as_view(success_url='/'),
         name='django_registration_register'),

]
