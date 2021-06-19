from django.shortcuts import render, redirect
from ..models import *

def saler(request):
    orders = Order.objects.all()
    context = {}
    context['orders'] = []
    for order in orders:
        orderItems = OrderItem.objects.filter(order=order)
        totalPrice = 0
        for orderItem in orderItems:
            totalPrice += orderItem.item.price * orderItem.qty
        order_item = str(orderItems[0].qty) + 'x' + orderItems[0].item.name
        if len(orderItems)-1 > 0:
            order_item += ' ... '
        context['orders'].append((order, order_item, totalPrice))
    context['orders'] = context['orders'][::-1]
    return render(request, 'manager/saler.html', context)

def confirmOrder(request, order_id):

    order = Order.objects.get(pk=order_id)
    order.statusNow = "Đã duyệt"
    order.save()

    member = Member.objects.get(pk=request.session.get('member'))
    # update order history
    updateOrderHistory(order, member)

    # notice to customer
    noticeCustomer(order, ' đã được chúng tôi tiếp nhận')

    return redirect('mystore:saler')

def cancelOrder(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.statusNow = "Đã hủy"
    order.save()

    member = Member.objects.get(pk=request.session.get('member'))
    # update order history
    updateOrderHistory(order, member)

    # notice to customer
    noticeCustomer(order, ' đã bị hủy')

    return redirect('mystore:saler')

def updateOrderHistory(order, member):
    updateStatus = OrderHistory(
        order=order, status=order.statusNow, member=member)
    updateStatus.save()


def noticeCustomer(order, content):
    # notice to customer
    notification = Notification()
    notification.customer = order.cart.customer
    notification.content = 'Đơn hàng mã ' + \
        str(order.id) + content
    notification.attach = 'saler/view-order/'+str(order.id)
    notification.save()
    

def viewOrder(request, order_id):
    context = {}
    order = Order.objects.get(id=order_id)
    orderItems = OrderItem.objects.filter(order=order)

    total = 0
    context['items'] = []
    context['qtyInStock'] = []
    for orderItem in orderItems:
        price = orderItem.qty * orderItem.item.price
        total += price
        product = orderItem.item.product
        context['items'].append((orderItem, price, product.qty_in_stock))
        context['qtyInStock'].append(product.qty_in_stock)

    customer = Member.objects.get(id=order.cart.customer.member.id)

    shipment = Shipment.objects.get(id=order.shipment.id)
    # shipper = Member.objects.get(id=shipment.shipper.member.id)
    context['deliveryAddress'] = order.deliveryAddress
    context['order'] = order
    context['customer'] = customer
    # context['shipper'] = shipper
    context['subtotal'] = total
    context['total'] = total + order.shipment.shipmentMethod.fee
    return render(request, 'manager/view-order.html', context)


def sendWarehouse(request, order_id):

    order = Order.objects.get(id=order_id)
    order.statusNow = 'Đợi kho'
    order.save()

    member = Member.objects.get(id=request.session.get('member'))
    updateStatus = OrderHistory(
        order=order, status=order.statusNow, member=member)
    updateStatus.save()    

    return redirect('mystore:saler')


def newProduct(request):
    categories = Category.objects.all()
    context = {}
    context['categories'] = []
    for category in categories:
        context['categories'].append(category)
    return render(request, template_name='manager/new-product.html', context=context)


def newProductDetail(request, type_id):
    context = {}
    context['type_id'] = type_id
    typee = Type.objects.get(pk=type_id)
    # attributes of product type
    typeAttributes = AttributeType.objects.filter(type=typee)

    context['attributes'] = typeAttributes
    print(typeAttributes)
    # all warehouses
    warehouses = Warehouse.objects.all()
    suppliers = Supplier.objects.all()
    context['suppliers'] = suppliers
    context['warehouses'] = warehouses
    return render(request, template_name='manager/new-product-detail.html', context=context)


def importProduct(request):

    member_id = request.session.get('member')
    member = Member.objects.get(pk=member_id)
    images = []

    for f in request.FILES.getlist('image'):
        images.append(f.name)

    warehouse_id = request.POST['warehouse']
    supplier_id = request.POST['supplier']
    product_name = request.POST['product-name']
    product_price = (float)(request.POST['price'])
    description = request.POST['description']
    quantity = int(request.POST['qty'])
    type_id = request.POST['type_id']

    # save product
    product = Product()
    product.warehouse = Warehouse.objects.get(pk=warehouse_id)
    product.supplier = Supplier.objects.get(pk=supplier_id)
    product.name = product_name
    product.price = product_price
    product.qty_in_stock = quantity
    product.description = description
    product.type = Type.objects.get(pk=type_id)

    product.save()

    # save images
    for img_name in images:
        image = Image()
        image.product = product
        image.path = img_name
        image.save()    

    attributes = AttributeType.objects.filter(
        type=Type.objects.get(pk=type_id))
    for attributeType in attributes:
        att_value = AttributeValue()
        att_value.product = product
        att_value.attribute = attributeType.attribute
        att_value.value = request.POST[str(attributeType.attribute.id)]
        # save product attribute value
        att_value.save()
    
    # save import file
    importBill = ImportBill()
    ImportBill.warehouseStaff = WarehouseStaff.objects.get(member=member)
    importBill.save()

    # save import product
    importProduct = ImportProduct()
    importProduct.product = product
    importProduct.import_bill = importBill
    importProduct.qty = quantity
    importProduct.save()

    return redirect("mystore:new-product")


def showFeedback(request):
    context = {}
    feedbacks = Feedback.objects.all()
    isProcessedFeedback = []
    for feedback in feedbacks:
        if feedback.isProcessed == True:
            isProcessedFeedback.append(feedback)
    processingFeedback = [
        fb for fb in feedbacks if fb not in isProcessedFeedback]
    print(isProcessedFeedback)
    context['processedFeedback'] = isProcessedFeedback[::-1]
    context['processingFeedback'] = processingFeedback[::-1]

    return render(request, template_name='manager/feedback.html', context=context)


def approveFeedback(request, feedback_id):
    feedback = Feedback.objects.get(pk=feedback_id)
    feedback.isProcessed = True
    feedback.save()
    return redirect('mystore:show-feedback')


def removeFeedback(request, feedback_id):
    Feedback.objects.filter(pk=feedback_id).delete()
    return redirect('mystore:show-feedback')


def showResponseComment(request, comment_id):
    return render(request, template_name='manager/response-comment.html',  context={'comment': Comment.objects.get(pk=comment_id)})


def responseComment(request, comment_id):
    
    member_id = request.session.get('member')
    member = Member.objects.get(pk=member_id)
    comment = Comment.objects.get(pk=comment_id)
    response = Respone()
    response.member = member
    response.comment = comment
    response.content = request.POST['content']
    print(comment)
    response.save()
    return redirect('mystore:show-feedback')
