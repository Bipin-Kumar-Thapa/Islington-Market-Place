from django.contrib import admin
from . models import Category, blog #this are the class name defined in model blog.

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):  #it is used to customize admin dashboard
    list_display = ('id','name')

class BlogAdmin(admin.ModelAdmin):
    exclude = ('created_at','updated_at')
    list_display = ('id','title','created_at','updated_at','published','category')

admin.site.register(Category, CategoryAdmin) #without this we cannot see classes in admin dashboard
admin.site.register(blog, BlogAdmin)