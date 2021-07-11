from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

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

# Create your views here.
class Logout(APIView):
    
    permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)
    
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response({"message":"You are logged out"}, status=status.HTTP_200_OK)
    
