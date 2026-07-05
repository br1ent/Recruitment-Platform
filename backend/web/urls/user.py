from django.urls import path
from web.views.auth.login import LoginView
from web.views.auth.register import RegisterView

urlpatterns = [
    path("api/auth/login/", LoginView.as_view(), name='login'),
    path("api/auth/register/", RegisterView.as_view(), name='register'),
]
