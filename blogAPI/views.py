from django.shortcuts import render
from rest_framework import viewsets

from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    lookup_field = 'slug'
    parser_classes = [FormParser, MultiPartParser]
    
    def get_queryset(self):
        return Post.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Category.objects.all()