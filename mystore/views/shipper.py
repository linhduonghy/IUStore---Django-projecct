from django.shortcuts import redirect, render
from django.template import Context, context
from django.db.models import Q
from ..models import *
from ..views import cart

def shipper(request):
    orders = Order.objects.filter(Q(statusNow='Đợi giao') | Q(statusNow='Đang giao')|Q(statusNow='Đã giao'))
    orderDone = Order.objects.filter(statusNow='Đã giao')
    context = {}
    context['orders'] = []
    context['orderDone'] = []
    context['items'] = []

    for order in orders:
        orderItems = OrderItem.objects.filter( order =order)
        order_item = str(orderItems[0].qty) + 'x' + orderItems[0].item.name
        if len(orderItems) > 1:
            order_item += ' ... '
        context['orders'].append((order,order_item))

    for order in orderDone:
        orderItems = OrderItem.objects.filter( order =order)
        order_item = str(orderItems[0].qty) + 'x' + orderItems[0].item.name
        if len(orderItems)-1 > 0:
            order_item += ' ... '
        context['orderDone'].append((order,order_item))

    context['orderDone'] = context['orderDone'][::-1]
    context['orders'] = context['orders'][::-1]    

    return render(request, 'manager/shipment.html',context)

def shipping (request,order_id):

    order = Order.objects.get(id = order_id)
    order.statusNow = 'Đang giao'
    print(order)
    
    print(order.statusNow)

    member = Member.objects.get(id = request.session.get('member'))
    print(member)
    updateStatus = OrderHistory()
    updateStatus.member = member
    updateStatus.order = order
    updateStatus.status = order.statusNow
    updateStatus.save()

    # shipper
    shipper = Shipper.objects.get(member=member)

    shipment = order.shipment
    shipment.shipper = shipper
    shipment.save()
    
    order.save()
    
    return redirect('mystore:shipper')

def finished (request,order_id):
    
    order = Order.objects.get(id = order_id)
    order.statusNow = 'Đã giao'
    order.save()

    member = Member.objects.get(id = request.session.get('member'))
    updateStatus = OrderHistory()
    updateStatus.member = member
    updateStatus.order = order
    updateStatus.status = order.statusNow
    updateStatus.save()

    # notice to customer
    notification = Notification()
    notification.customer = order.cart.customer
    notification.content = 'Đơn hàng mã ' + \
        str(order.id) + ' đã được giao thành công'
    notification.attach = 'saler/view-order/'+str(order.id)
    notification.save()
    return redirect('mystore:shipper')