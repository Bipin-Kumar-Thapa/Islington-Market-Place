from django.shortcuts import render
from django.http import HttpResponse
from . models import blog, Category
from django.shortcuts import render, get_object_or_404

# Create your views here.

def blogs(request):
    Blog = blog.objects.all()
    return render(request,'blogs/blogs1.html',{'Blog':Blog})

def blogdetails(request, id):
    Blog = get_object_or_404(blog, id=id)
    return render(request, 'blogs/details1.html',{'Blog':Blog})



