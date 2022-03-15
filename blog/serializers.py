from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Category, Post
from django.contrib.auth.models import User

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name',)
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']


class PostLVSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'nazvanie', 'data_sozdania','users']


class PostDVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'nazvanie', 'data_sozdania', 'text_posta', 'img_path')

    img_path = serializers.SerializerMethodField()

    def get_img_path(self, obj):
        if obj.img:
            return obj.img.url


