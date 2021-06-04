from os import name
from ..views.product import product
from django.shortcuts import render
from ..models import *

def showItemDetail(request, item_id):
    item = Item.objects.get(id=item_id)
    discount = Discount.objects.get(id=item_id)

    discout_price = discount.discount_value
    current_price = item.price
    discount_rate = round(discout_price / current_price * 100) - 100
    
    attribute_values = AttributeValue.objects.filter(product=item.product)
    attrs = []
    attr_values = []
    for i in attribute_values:
        attrs.append(Attribute.objects.get(id=i.attribute.id))
        attr_values.append(i.value)

    context = {}
    context['item'] = item
    context['product'] = item.product
    context['current_price'] = current_price
    context['discount_price'] = discout_price
    context['discount_rate'] = discount_rate
    context['attrs'] = attrs
    context['attribute_values'] = attr_values

    return render(request, "item_detail.html", context)


def searchItem(request):

    query = request.GET['q']
    # get list product relevance
    return render(request, 'search_item.html')