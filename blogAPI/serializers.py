from rest_framework import serializers

from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'user', 'category', 'slug', 'public', 'photo')
        lookup_field = 'slug'
        
        
class UserPostSerializer(serializers.ModelSerializer):
    
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'user', 'category', 'slug', 'public', 'photo')
        lookup_field = 'slug'
  