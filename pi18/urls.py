"""pi18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from blog import views
from blog.api import post_detail, post_list, user_list, product_detail,product_list, cell_detail,cell_list,category_detail,category_list,shelf_detail,shelf_list,arrival_detail,arrival_list,expenditure_detail,expenditure_list
from blog.views import render_home

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
#router.register(r'post', views.PostViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',render_home),
     path('api-auth/', include('rest_framework.urls')),
    #path('', include(router.urls)), 
    path('posts/',  post_list),
    path('posts/<int:pk>/', post_detail),
    path('users/',user_list),
    
    path('products/',  product_list),
    path('products/$<int:pk>/', product_detail),
    
    path('shelves/',  shelf_list),
    path('shelves/<int:pk>/', shelf_detail),
    
    path('cells/',  cell_list),
    path('cells/<int:pk>/', cell_detail),
    
    path('arrivals/',  arrival_list),
    path('arrivals/<int:pk>/', arrival_detail),
    
    path('expenditure/',  expenditure_list),
    path('expenditure/<int:pk>/', expenditure_detail),
    
    
    path('categories/',  category_list),
    path('categories/$<int:pk>/',  category_detail),

    
    ]

