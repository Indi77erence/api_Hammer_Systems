from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework import mixins
from rest_framework import generics


class UserList(mixins.ListModelMixin,
			   mixins.CreateModelMixin,
			   generics.GenericAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class UserProfile(mixins.RetrieveModelMixin,
				 mixins.UpdateModelMixin,
				 mixins.DestroyModelMixin,
				 generics.GenericAPIView,):

	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		data = request.data
		user = User.objects.get(phone_number=data['phone_number'])
		if not user.activated_invite_code:
			code = data['activated_invite_code']
			invited_user = User.objects.get(invite_code=code)
			invited_user.add_activated_invite_code(user.phone_number)
			return self.update(request, *args, **kwargs)
		else:
			return Response({"error": "You have already activated invite code."}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
