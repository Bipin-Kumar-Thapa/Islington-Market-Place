from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category,Product  # Correct import path
from blogs.models import blog, Category



def home(request):
    products = Product.objects.all()
    Blog = blog.objects.all()[:3]
    return render(request,'home/home1.html',{'products':products, 'Blog':Blog})


