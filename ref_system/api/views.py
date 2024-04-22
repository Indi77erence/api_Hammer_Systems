from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer


class UserProfileAPIView(APIView):
    def get(self, request, phone_number):
        try:
            user = User.objects.get(phone_number=phone_number)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise NotFound("User not found")

    def patch(self, request, phone_number):
        try:
            invite_code = request.data.get('invite_code')
            invited_user = User.objects.get(invite_code=invite_code)
            user = User.objects.get(phone_number=phone_number)
            if not user.activated_invite_code:
                user.set_invite_code(invite_code=invite_code)
                invited_user.add_activated_invite_code(user.phone_number)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response({"error": "You have already activated invite code."}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "User with this invite code does not exist."}, status=status.HTTP_404_NOT_FOUND)
