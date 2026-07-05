from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from web.models.user import UserProfile


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email', '').strip()
        password = request.data.get('password', '').strip()

        if not email or not password:
            return Response({
                "message": "邮箱和密码不能为空"
            })

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({
                "message": "邮箱或密码错误"
            })

        user = authenticate(username=user_obj.username, password=password)

        if user is None:
            return Response({
                "message": "邮箱或密码错误"
            })

        if not user.is_active:
            return Response({
                "message": "账号已被禁用"
            })

        profile = UserProfile.objects.get(user=user)
        refresh = RefreshToken.for_user(user)

        response = Response({
            "message": "success",
            "access_token": str(refresh.access_token),
            "user_id": user.id,
            "email": user.email,
            "phone": profile.phone,
            "avatar": profile.avatar.url if profile.avatar else None,
            "resume": profile.resume.url if profile.resume else None,
            "role": profile.role,
            "status": profile.status,
        })

        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            samesite="Lax",
            secure=True,
            max_age=86400 * 7,
        )

        return response
