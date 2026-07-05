from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.user import UserProfile

class GetInfoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(user=user)

            return Response({
                "message": "success",
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "phone": user_profile.phone,
                "avatar": user_profile.avatar.url,
                "resume": user_profile.resume.url if user_profile.resume else None,
                "role": user_profile.role,
                "status": user_profile.status,
            })
        except:
            return Response({
                "message": "系统出错了，请稍后重试!"
            })