from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),  # This handles /cart/ because you include it in main urls.py
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    # other cart URLs if needed
]

