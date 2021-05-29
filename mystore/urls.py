from django.urls import path
from .view import index, cart, product

app_name = 'mystore'

urlpatterns = [
    path('', index.home, name='home'),
    path('cart', cart.cart, name = 'cart'),
    path('product/<product_id>', product.showProductDetail, name='product-detail'),
]
