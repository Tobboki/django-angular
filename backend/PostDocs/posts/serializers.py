from rest_framework import serializers
from .models import Post ,User,comment

class post_serializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields=['id','title','content','user']

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'firstname', 'lastname', 'email']

class comment_serializer(serializers.ModelSerializer):
    class Meta:
        model= comment
        fields = ['id', 'content', 'post','user']

