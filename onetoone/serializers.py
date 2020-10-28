from rest_framework import serializers
from .models import Post, PostRates

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'post_title', 'post_body', 'rates')
        depth = 1

class PostRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRates
        fields = ('id', 'likes', 'dislikes')

