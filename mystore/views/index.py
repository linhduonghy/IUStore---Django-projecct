from django.shortcuts import render
from django.template import Context, context
from ..models import *


def home(request):
    items = Item.objects.all()
    context = {}


    context['items'] = []

    
    for item in items:
        product = item.product
        product_images = Image.objects.filter(product=product)
        context['items'].append((item,product_images[0].path))
    
    
    return render(request, 'home.html',context)