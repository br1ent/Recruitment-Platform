from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

from web.models.user import UserProfile


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username', '').strip()
        email = request.data.get('email', '').strip()
        password = request.data.get('password', '').strip()
        confirm_password = request.data.get('confirm_password', '').strip()

        # 参数校验
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

        # 查重
        if User.objects.filter(username=username).exists():
            return Response({
                "message": "该用户名已经被别人使用了，再换一个试试吧"
            })

        if User.objects.filter(email=email).exists():
            return Response({
                "message": "该邮箱已经注册过了"
            })

        # 创建用户和用户档案
        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user)

        return Response({
            "message": "success"
        })
