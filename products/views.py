from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(request):
    products = Product.objects.all() #it wil fetch all the product from database
    return render(request,'products/products1.html',{'products':products})  #{'products':products}: It is been used to send value to the template from the view. It is a context dict(passing value from view to template).

def product_detail(request, id): #it will handle request of the specific product on the basis of unique id
    product = get_object_or_404(Product, id=id ) #it retrive object from the database with the specific id.
    return render(request,'products/details1.html',{'product':product}) 