from django.urls import path
from .views import index, cart, product, user,customer,payment,manage

app_name = 'mystore'

urlpatterns = [
    path('', index.home, name='home'),
    path('cart', cart.cart, name = 'cart'),
    path('login', user.login, name='login'),
    path('logout', user.logout, name='logout'),
    path('customer/notification', customer.notification, name='notification'),
    path('customer/info', customer.info, name='info'),
    path('customer/order', customer.order, name='customer-order'),
    path('product/<product_id>', product.showProductDetail, name='product-detail'),
    path('search', product.searchProduct, name='search-product'),
    path('checkout', payment.checkout, name='checkout'),

    # manager
    path('saler', manage.saler, name = 'saler'),
    path('shipment', manage.shipment, name = 'shipment'),
    path('registation', user.register, name = 'register'),
    path('new-product', manage.newProduct, name = 'new-product'),
    path('new-product/new-book-detail', manage.newBookDetail, name = 'new-book-detail'),
    path('new-product/new-electro-detail', manage.newElectroDetail, name = 'new-electro-detail'),
    path('new-product/new-clothes-detail', manage.newClothesDetail, name = 'new-clothes-detail'),
]
