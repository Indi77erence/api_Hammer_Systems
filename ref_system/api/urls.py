from django.urls import path

from .auth.auth_user import login_view, create_user, auth_user
from .views import UserProfileAPIView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('create_user/', create_user, name='create_user'),
    path('auth_user/', auth_user, name='auth_user'),
    path('user_profile/<str:phone_number>/', UserProfileAPIView.as_view(), name='user_profile'),
]
