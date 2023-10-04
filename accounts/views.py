from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import csrf_exempt



User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        token = Token.objects.create(user=user)
        response = Response({'token': token.key})
        response.set_cookie('auth_token', token.key, httponly=True)
        return response

class ObtainAuthTokenWithCookie(ObtainAuthToken):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            token = Token.objects.get(key=response.data['Token'])
            response.set_cookie('auth_token', token.key, httponly=True)
        return response