from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category,Product  # Correct import path
from blogs.models import blog, Category



def home(request):
    products = Product.objects.all().filter(status = True)
    #banners = Banner.objects.all().filter(status = True)
    #categories = Category.objects.all().filter(status = True)
    #Blog = blog.objects.all()[:3]
    context = {
        'products': products,
        #'banners': banners,
        #'categories': categories
    }
    return render(request,'home/home1.html', context)

def cart(request):
    return render(request,'cart/cart.html')

def checkout(request):
    return render(request,'orders/checkout.html')

def place_order(request):
    return render(request,'orders/place_order.html')

def order_complete(request):
    return render(request,'orders/order_complete.html')

def my_orders(request):
    return render(request,'orders/my_orders.html')

def dashboard(request):
    return render(request,'user/dashboard.html')

def login(request):
    return render(request,'user/login.html')

def register(request):
    return render(request,'user/register.html')

def change_password(request):
    return render(request,'user/change_password.html')

def edit_profile(request):
    return render(request,'user/edit_profile.html')

def product_details(request):
    return render(request,'products/product1_details.html')

def category(request):
    return render(request,'products/category.html')