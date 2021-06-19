from django.shortcuts import redirect, render
from django.template import Context, context
from ..models import *

def product(request):

    products = Product.objects.all()
    context = {}
    context['products'] = products
    return render(request, 'manager/product.html',context)


def showProductDetail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, template_name='manager/product_detail.html', context={'product': product})
    
def active(request):
    items = Item.objects.all()
    products =[]
    for item in items:
        products.append(item.product)
    context = {}
    context['products'] = products
    context['msg'] = 'active'
    return render(request, 'manager/product.html',context)

def checkExist(product, items):
    for item in items:
        if item.product.id == product.id:
            return False
    return True
def getUnSoldProduct(request):
    context = {}
    items = Item.objects.all()
    products = Product.objects.all()

    prs = []
    for product in products:
        if checkExist(product, items):
            prs.append(product)
    
    context['products'] = prs
    return render(request, 'manager/up-shelf.html', context)

def putItemDetail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {}
    context['product'] = product
    return render(request, template_name='manager/put-item-detail.html', context=context)

def handlePutItem(request, product_id):
    product = Product.objects.get(pk=product_id)
    item = Item()
    item.product = product
    item.name = product.name
    item.price = product.price
    item.save()

    discount = Discount()
    discount.discount_value = request.POST['discountValue']
    discount.from_date = request.POST['fromDate']
    discount.item = item
    discount.save()
    return redirect('mystore:product')

def upShelf(request, product_id):
    product = Product.objects.get(pk=product_id)
    item = Item()
    item.product = product
    item.name = product.name
    item.price = product.price
    item.save()

    discount = Discount()
    discount.discount_value = request.POST['discountValue']
    discount.from_date = request.POST['fromDate']
    discount.item = item
    discount.save()
    return redirect('mystore:product')