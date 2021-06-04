from django.shortcuts import render, redirect
from ..models import *

def saler(request):
    orders = Order.objects.all()
    context = {}
    context['orders'] = []
    for order in orders:
        cart_items = CartItem.objects.filter( cart =order.cart)
        order_item = str(cart_items[0].qty) + ' ' + cart_items[0].item.name
        if len(cart_items)-1 > 0:
            order_item += ' và ' +  str(len(cart_items)-1)+' các sản phẩm khác'
        order_item = str(cart_items[0].qty) + ' ' + cart_items[0].item.name
        context['orders'].append((order,order_item))
    return render(request, 'manager/saler.html',context)

def shipment(request):
    return render(request, 'manager/shipment.html')

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
    context['warehouses'] = warehouses
    return render(request, template_name='manager/new-clothes-product.html', context=context)

def importProduct(request):
    
    warehouse_id = request.POST['warehouse']
    product_name = request.POST['product-name']
    product_price = (float)(request.POST['price'])
    description = request.POST['description']
    quantity = int(request.POST['qty'])
    type_id = request.POST['type_id']

    # save product
    product = Product()
    product.warehouse = Warehouse.objects.get(pk=warehouse_id)
    product.name = product_name
    product.price = product_price
    product.qty_in_stock = quantity
    product.type = Type.objects.get(pk=type_id)
    
    product.save()
    
    # save import file
    importFile = ImportFile()
    importFile.save()

    # save import product
    importProduct = ImportProduct()
    importProduct.product = product
    importProduct.import_file = importFile
    importProduct.qty = quantity
    importProduct.save()

    attributes = AttributeType.objects.filter(type = Type.objects.get(pk=type_id))
    for attributeType in attributes:
        att_value = AttributeValue()
        att_value.product = product
        att_value.attribute = attributeType.attribute
        att_value.value = request.POST[str(attributeType.attribute.id)]
        # save product attribute value
        att_value.save()
    
    return redirect("mystore:new-product")

def newBookDetail(request):
    context = {}
    if request.POST:
        img1 = request.POST.get('image1')
        name = request.POST.get('name')
        published_date = request.POST.get('publishedDate')
        author = request.POST.get('author')
        pages = request.POST.get('pages')
        publisher = request.POST.get('publisher')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        released_company = request.POST.get('released')

        height = request.POST.get('height')
        width = request.POST.get('width')
        length = request.POST.get('length')
        demension = length + "x" + width + "x" + height + " mm"
        cover = request.POST.get('status')

        product = Product()

    return render(request, 'manager/new-book-product.html')

def newElectroDetail(request):
    return render(request, 'manager/new-electro-product.html')

def newClothesDetail(request):
    return render(request, 'manager/new-clothes-product.html')

def sendWarehouse(request,order_id):

    order = Order.objects.get(id = order_id)
    order.statusNow = 'Đợi kho'
    order.save()

    member = Member.objects.get(id = request.session.get('member'))

    updateStatus = OrderHistory(order=order,status=order.statusNow,member=member)

    updateStatus.save()

    return redirect('mystore:saler')