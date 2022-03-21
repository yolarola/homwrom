from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Category, Post, Product, Arrival,Expenditure,Cell,Shelf
from django.contrib.auth.models import User

class CategorySerializerLV(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name',)
        
class CategorySerializerDV(serializers.HyperlinkedModelSerializer):
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
        
        

class ProductSerializerLV(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','price','category','structure','weight','color','size')


class ProductSerializerDV(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','price','category','structure','weight','color','size')
    


class ShelfSerializerLV(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shelf
        fields = ('id','number','block')
        
class ShelfSerializerDV(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shelf
        fields = ('id','number','block','row','place')
        
class CellSerializerLV(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cell
        fields = ('id','shelf','product')
        
class CellSerializerDV(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cell
        fields = ('id','shelf','volume','product','quantity')
        

class ArrivalSerializerLV(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Arrival
        fields = ('id','date','product')
        
class ArrivalSerializerDV(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Arrival
        fields = ('id','date','product','suplier','quantity')
        

class ExpenditureSerializerLV(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expenditure
        fields = ('id','date','product')
        
class ExpenditureSerializerDV(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expenditure
        fields = ('id','date','product','suplier','quantity')
        
        
