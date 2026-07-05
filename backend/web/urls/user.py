from django.contrib.auth.views import LogoutView
from django.urls import path

from web.views.auth.get_info import GetInfoView
from web.views.auth.login import LoginView
from web.views.auth.refresh_token import RefreshTokenView
from web.views.auth.register import RegisterView
from web.views.auth.reset_pwd import ResetPwdView

urlpatterns = [
    path("api/auth/login/", LoginView.as_view(), name='login'),
    path("api/auth/register/", RegisterView.as_view(), name='register'),
    path("api/auth/resetpwd/", ResetPwdView.as_view(), name='reset_password'),
    path("api/auth/get_info/", GetInfoView.as_view(), name='get_info'),
    path("api/auth/logout/", LogoutView.as_view(), name='logout'),
    path("api/auth/refresh/", RefreshTokenView.as_view(), name='refresh'),
]
