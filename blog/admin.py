from django.contrib import admin

# Register your models here.
from blog.models import Arrival, Category, Cell, Expenditure, Post, PhotoPostov,Product, Shelf

class PhotoPostovInline(admin.TabularInline):
    model = PhotoPostov
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'nazvanie', 'user', 'data_sozdania']
    search_fields = ['id', 'nazvanie', 'user', 'text_posta']
    list_filter = ['user','data_sozdania']
    inlines = [PhotoPostovInline,]

    save_as = True
    save_on_top = True
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Shelf)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','number','block','row','place']

@admin.register(Cell)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','shelf','volume']

@admin.register(Arrival)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','date','product']

@admin.register(Expenditure)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','date','product']