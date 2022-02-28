from django.contrib import admin

# Register your models here.
from blog.models import Post, PhotoPostov,Product

class PhotoPostovInline(admin.TabularInline):
    model = PhotoPostov
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'nazvanie', 'avtor', 'data_sozdania']
    search_fields = ['id', 'nazvanie', 'avtor', 'text_posta']
    list_filter = ['avtor','data_sozdania']
    inlines = [PhotoPostovInline,]

    save_as = True
    save_on_top = True
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name']