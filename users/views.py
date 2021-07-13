from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import CustomAuthTokenSerializer, RegisterUserSerializer


class RegisterUser(APIView):
    permission_classes = [AllowAny,]
    
    def post(self, request):
        reg_serializer = RegisterUserSerializer(data = request.data)
        if reg_serializer.is_valid():
            user = reg_serializer.save()
            if user:
                return Response({"message":"User registration succesful"}, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 
                         'user_id': user.pk,
                         'email': user.email})

# Create your views here.
class Logout(APIView):
    
    permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)
    
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response({"message":"You are logged out"}, status=status.HTTP_200_OK)
    
