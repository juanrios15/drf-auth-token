from django.shortcuts import render

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
# Create your views here.


class IsOwner(permissions.BasePermission):
    
      def has_object_permission(self, request, view, obj):

        return obj.user == request.user


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    lookup_field = 'slug'
    parser_classes = [FormParser, MultiPartParser]
    
    def get_queryset(self):
        return Post.objects.all()

    def get_permissions(self):
        
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Category.objects.all()
    
    def get_permissions(self):
        
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]