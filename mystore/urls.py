from django.urls import path
from .views import index, cart, product, user

app_name = 'mystore'

urlpatterns = [
    path('', index.home, name='home'),
    path('cart', cart.cart, name = 'cart'),
    path('login', user.login, name='login'),
    path('logout', user.logout, name='logout'),
    path('product/<product_id>', product.showProductDetail, name='product-detail'),
    path('search', product.searchProduct, name='search-product'),
]
