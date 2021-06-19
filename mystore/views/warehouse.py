from django.shortcuts import redirect, render
from django.template import Context, context
from ..models import *
from ..views import cart

def warehouse(request):
    orders = Order.objects.filter(statusNow='Đợi kho')
    context = {}
    context['orders'] = []
    for order in orders:
        orderItems = OrderItem.objects.filter( order =order)
        order_item = str(orderItems[0].qty) + 'x' + orderItems[0].item.name
        if len(orderItems)-1 > 0:
            order_item += ' ...'
        context['orders'].append((order,order_item))

    return render(request, 'manager/warehouse.html',context)

def exportProduct(request,order_id):
    
    member_id = request.session.get('member')
    member = Member.objects.get(id = request.session.get('member'))
    member = Member.objects.get(pk=member_id)
    order = Order.objects.get(id = order_id)
    orderItems = OrderItem.objects.filter( order =order)

    # update order
    order.statusNow = 'Đợi giao'
    order.save()
    
    updateStatus = OrderHistory()
    updateStatus.member = member
    updateStatus.order = order
    updateStatus.status = order.statusNow
    updateStatus.save()

    # update product qty in stick
    for orderItem in orderItems :
        product=Product.objects.get(id=orderItem.item.product.id)
        product.qty_in_stock -= orderItem.qty
        product.save()
    
    # export bill
    exportBill = ExportBill()
    exportBill.warehouseStaff = WarehouseStaff.objects.get(member=member)
    exportBill.save()
    for orderItem in orderItems:
        exportProduct = ExportProduct()
        exportProduct.export_bill = exportBill
        exportProduct.product = orderItem.item.product
        exportProduct.qty = orderItem.qty
        exportProduct.save()

    return redirect('mystore:warehouse')