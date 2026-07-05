from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response


class ResetPwdView(APIView):
    def post(self, request):
        username = request.data.get('username', '')
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        confirm_password = request.data.get('confirm_password', '')

        if not username:
            return Response({
                "message": "用户名不能为空"
            })

        if not email:
            return Response({
                "message": "邮箱不能为空"
            })

        if not password:
            return Response({
                "message": "密码不能为空"
            })

        if password != confirm_password:
            return Response({
                "message": "两次输入的密码不一致"
            })

        try:
            user = User.objects.get(username=username, email=email)
        except User.DoesNotExist:
            return Response({
                "message": "用户名或邮箱错误，请确认用户名和邮箱"
            })

        user.set_password(password)
        user.save()

        return Response({
            "message": "success"
        })
