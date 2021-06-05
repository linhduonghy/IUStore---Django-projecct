from django.shortcuts import redirect, render
from django.template import Context, context
from ..models import *

def product(request):

    products = Product.objects.all()
    context = {}
    context['products'] = products
    return render(request, 'manager/product.html',context)

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
def getList(request):
    context = {}
    items = Item.objects.all()
    products = Product.objects.all()

    prs = []
    for product in products:
        if checkExist(product, items):
            prs.append(product)
    
    context['up'] = prs
    return render(request, 'manager/up-shelf.html', context)

def upShelf(request, product_id):
    print(product_id)
    product = Product.objects.get(id=product_id)
    item = Item()
    item.product = product
    item.name = product.name
    item.price = product.price
    item.save()
    return redirect('mystore:product')