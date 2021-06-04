from ..models import *
from django.shortcuts import render


def notification(request):
    return render(request, 'customer/notification.html')


def info(request):
    return render(request, 'customer/user-info.html')


def order(request):
    context = {}
    context['orders'] = []
    
    member = Member.objects.get(id=request.session.get('member'))
    print(member)
    customer = Customer.objects.get(member=member)

    carts = Cart.objects.filter(customer = customer,is_order='True')
    print(carts)
    
    for cart in carts:
        
        order = Order.objects.get(cart=cart)
        
        cart_items = CartItem.objects.filter( cart = cart)
        order_item = str(cart_items[0].qty) + ' ' + cart_items[0].item.name
        if len(cart_items)-1 > 0:
            order_item += ' và ' +  str(len(cart_items)-1)+' các sản phẩm khác'
        order_item = str(cart_items[0].qty) + ' ' + cart_items[0].item.name
        context['orders'].append((order,order_item))

    return render(request, 'customer/order.html',context)