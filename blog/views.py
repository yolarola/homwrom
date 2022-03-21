from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializers import CategorySerializerLV,CategorySerializerDV, PostLVSerializer
from .models import Category, Post

def render_home(request):
    return render(request, 'blog/home_page.html')

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializerLV




    

