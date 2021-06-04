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