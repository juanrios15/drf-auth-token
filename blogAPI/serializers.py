from rest_framework import serializers

from .models import Post, Category
from users.serializers import UserDetailSerializer

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()
    user = UserDetailSerializer()
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'user', 'category', 'slug', 'public')
        lookup_field = 'slug'
  