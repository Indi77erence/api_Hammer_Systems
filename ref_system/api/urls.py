from django.urls import path

from .auth.auth_user import login_view, create_user, auth_user
from .views import UserProfile, UserList

urlpatterns = [
    path('login/', login_view, name='login'),
    path('create_user/', create_user, name='create_user'),
    path('auth_user/', auth_user, name='auth_user'),
    path('users/', UserList.as_view(), name='users'),
    path('user/<int:pk>/', UserProfile.as_view(), name='user'),
]
