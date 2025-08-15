from django.http import Http404
from .models import Product
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from carts.models import CartItem
from carts.views import _cart_id
from .models import Category

# Create your views here.

def index(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, status=True)
    else:
        products = Product.objects.all().filter(status=True).order_by('id')

        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = len(paged_products)

    # Ensure this block is indented correctly:
    for product in paged_products:
        product.low_stock = product.stock <= 5  # Add the low_stock attribute

    context = {
        'products': paged_products,
        'product_count': product_count,
    }

    return render(request, 'products/products1.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()

        is_out_of_stock = product.stock <= 0
        is_low_stock = 0 < product.stock <= 5
        
    except Product.DoesNotExist:
        raise Http404("Product Not Found")
    context = {
        'product': product,
        'in_cart': in_cart
    }
    return render(request, 'products/product1_details.html',context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword','').strip()
        products = Product.objects.none()
        if keyword:
            products = Product.objects.orderby('-created_date').filter(
                Q(description__icontains=keyword) | Q(name__icontains=keyword)
            )
    context = {
        'products':products,
        'product_count': products.count()
    }
    return render(request,'products/products1.html', context)