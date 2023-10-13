from django.urls import path,include
from .views import UserCreateAPIView, ObtainAuthTokenWithCookie, UserRetrieveUpdateAPIView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', ObtainAuthTokenWithCookie.as_view(), name='api_token_auth'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('profile/', UserRetrieveUpdateAPIView.as_view(), name='profile'),
]
