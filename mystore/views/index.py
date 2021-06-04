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
        discount = Discount.objects.get(id=item.id)
        discount_rate = round(discount.discount_value / item.price * 100) - 100
        context['items'].append((item,product_images[0].path, discount_rate))
    
    return render(request, 'home.html',context)