from django.urls import path,include
from .views import UserCreateAPIView,ObtainAuthTokenWithCookie
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', ObtainAuthTokenWithCookie.as_view(), name='api_token_auth'),

]
