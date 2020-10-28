from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Post, PostRates
from .serializers import PostRatesSerializer,PostSerializer

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_rates = PostRates.objects.create(likes = post_data["rates"]["likes"], dislikes=post_data["rates"]["dislikes"])
        new_rates.save()

        new_post = Post.objects.create(post_title=post_data["post_title"],post_body=post_data["post_body"],rates=new_rates)
        new_post.save()
        
        serializer = PostSerializer(new_post)

        return Response(serializer.data)





class PostRatesView(viewsets.ModelViewSet):
    queryset = PostRates.objects.all()
    serializer_class = PostRatesSerializer




