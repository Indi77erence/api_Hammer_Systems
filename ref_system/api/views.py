from django.core.exceptions import ObjectDoesNotExist
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

	def patch(self, request, *args, **kwargs):
		try:
			invite_code = request.data['activated_invite_code']
			if invite_code:
				invited_user = User.objects.get(invite_code=invite_code)
				invited_user.add_activated_invite_code(request.data['phone_number'])
				return self.partial_update(request, *args, **kwargs)
			return self.update(request, *args, **kwargs)
		except ObjectDoesNotExist:
			return Response({'error': 'Пользователь с таким invite_code не найден'}, status=status.HTTP_404_NOT_FOUND)


	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
