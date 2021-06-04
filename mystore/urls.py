from django.urls import path
from .views import index, cart, item, user,customer,payment,manage,types,product

app_name = 'mystore'

urlpatterns = [
    path('', index.home, name='home'),
    path('cart', cart.cart, name = 'cart'),
    path('add-to-cart', cart.addToCart, name='add-to-cart'),
    path('cart/delete/<item_id>', cart.deleteItem, name='cart/delete'),
    path('login', user.login, name='login'),
    path('logout', user.logout, name='logout'),
    path('customer/notification', customer.notification, name='notification'),
    path('customer/info', customer.info, name='info'),
    path('customer/order', customer.order, name='customer-order'),
    path('item/<item_id>', item.showItemDetail, name='item-detail'),
    path('search', item.searchItem, name='search-item'),
    path('checkout', payment.checkout, name='checkout'),
    path('type/category', types.getTypeByCategory, name='type-by-category'),
    path('product', product.product, name = 'product'),
    path('product/active', product.active, name = 'product-active'),
    # manager
    path('saler', manage.saler, name = 'saler'),
    path('shipment', manage.shipment, name = 'shipment'),
    path('registation', user.register, name = 'register'),
    path('new-product', manage.newProduct, name = 'new-product'),
    path('new-product-detail/type/<int:type_id>', manage.newProductDetail, name='new-product-detail'),
    path('import-product', manage.importProduct, name='import-product'),
    path('new-product/new-book-product', manage.newBookDetail, name = 'new-book-product'),
    path('new-product/new-electro-product', manage.newElectroDetail, name = 'new-electro-product'),
    path('new-product/new-clothes-product', manage.newClothesDetail, name = 'new-clothes-product'),
]
