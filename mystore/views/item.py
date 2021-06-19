from os import name
from ..views.product import product
from django.shortcuts import render, redirect
from ..models import *


def showItemDetail(request, item_id):

    context = {}
    item = Item.objects.get(pk=item_id)
    product = item.product
    product_images = Image.objects.filter(product=product)
    if product_images.count() > 0:
        img = product_images[0].path
    else:
        img = None
    context['img_path'] = img

    discount_rate = None
    discout_price = None
    try:
        discount = Discount.objects.get(item=item)
        discout_price = discount.discount_value
        discount_rate = round(discount.discount_value / item.price * 100) - 100
    except Discount.DoesNotExist:
        pass

    current_price = item.price

    attribute_values = AttributeValue.objects.filter(product=item.product)
    attrs = []
    attr_values = []
    for i in attribute_values:
        attrs.append(Attribute.objects.get(id=i.attribute.id))
        attr_values.append(i.value)

    # feedback
    fbs = []
    feedbacks = getFeedback(item)
    fb_count = sum(1 for feedback in feedbacks if feedback.isProcessed == True)
    if fb_count == 0:
        rate_avg = None
    else:
        rate_avg = sum(feedback.rate_score for feedback in feedbacks if feedback.isProcessed == True) / fb_count
    context['rate_avg'] = rate_avg

    for feedback in feedbacks:
        if feedback.isProcessed == False:
            continue
        responses = Respone.objects.filter(comment=feedback.comment)
        rate = [1 for _ in range(feedback.rate_score)]
        fbs.append((feedback, rate, responses))

    context['item'] = item
    context['exportCount'] = getExportCount(item)
    context['product'] = item.product
    context['current_price'] = current_price
    context['discount_price'] = discout_price
    context['discount_rate'] = discount_rate
    context['attrs'] = attrs
    context['attribute_values'] = attr_values
    context['feedbacks'] = fbs[::-1]

    # similar items
    context['items'] = []
    items = getSimilarItem(item_id)
    for item in items:
        product = item.product
        product_images = Image.objects.filter(product=product)
        if product_images.count() > 0:
            img = product_images[0].path
        else:
            img = None
        discount_rate = None
        discount = None
        try:
            discount = Discount.objects.get(item=item)
            discount_rate = round(
                discount.discount_value / item.price * 100) - 100
        except Discount.DoesNotExist:
            pass
        
        feedbacks = Feedback.objects.filter(item=item)
        fb_count = sum(1 for feedback in feedbacks if feedback.isProcessed == True)
        if fb_count == 0:
            rate_avg = 0
            fb_count = None
        else:
            rate_avg = sum(feedback.rate_score for feedback in feedbacks if feedback.isProcessed == True) / fb_count
        exportCount = getExportCount(item)
        context['items'].append((item,img, discount,discount_rate,rate_avg, fb_count, exportCount))

    return render(request, "item_detail.html", context)

def showItemComment(request, item_id):
    context = {}
    item = Item.objects.get(pk=item_id)
    product = item.product
    product_images = Image.objects.filter(product=product)
    if product_images.count() > 0:
        img = product_images[0].path
    else:
        img = None
    context['img_path'] = img

    discount_rate = None
    discout_price = None
    try:
        discount = Discount.objects.get(item=item)
        discout_price = discount.discount_value
        discount_rate = round(discount.discount_value / item.price * 100) - 100
    except Discount.DoesNotExist:
        pass

    current_price = item.price

    attribute_values = AttributeValue.objects.filter(product=item.product)
    attrs = []
    attr_values = []
    for i in attribute_values:
        attrs.append(Attribute.objects.get(id=i.attribute.id))
        attr_values.append(i.value)

    # feedback
    fbs = []
    feedbacks = getFeedback(item)
    fb_count = sum(1 for feedback in feedbacks if feedback.isProcessed == True)
    if fb_count == 0:
        rate_avg = None
    else:
        rate_avg = sum(feedback.rate_score for feedback in feedbacks if feedback.isProcessed == True) / fb_count
    context['rate_avg'] = rate_avg

    for feedback in feedbacks:
        if feedback.isProcessed == False:
            continue
        responses = Respone.objects.filter(comment=feedback.comment)
        rate = [1 for _ in range(feedback.rate_score)]
        fbs.append((feedback, rate, responses))

    context['item'] = item
    context['exportCount'] = getExportCount(item)
    context['product'] = item.product
    context['current_price'] = current_price
    context['discount_price'] = discout_price
    context['discount_rate'] = discount_rate
    context['attrs'] = attrs
    context['attribute_values'] = attr_values
    context['feedbacks'] = fbs[::-1]

    # similar items
    context['items'] = []
    items = getSimilarItem(item_id)
    for item in items:
        product = item.product
        product_images = Image.objects.filter(product=product)
        if product_images.count() > 0:
            img = product_images[0].path
        else:
            img = None
        discount_rate = None
        discount = None
        try:
            discount = Discount.objects.get(item=item)
            discount_rate = round(
                discount.discount_value / item.price * 100) - 100
        except Discount.DoesNotExist:
            pass
        
        fb_count = sum(1 for feedback in feedbacks if feedback.isProcessed == True)
        if fb_count == 0:
            rate_avg = 0
            fb_count = None
        else:
            rate_avg = sum(feedback.rate_score for feedback in feedbacks if feedback.isProcessed == True) / fb_count
        exportCount = getExportCount(item)
        context['items'].append((item,img, discount,discount_rate,rate_avg, fb_count, exportCount))   
    context['comment'] = True
    return render(request, "item_detail.html", context)

def getFeedback(item):
    return Feedback.objects.filter(item=item)

def getExportCount(item):
    exportProducts = ExportProduct.objects.filter(product=item.product)
    exportCount = sum(exportProduct.qty for exportProduct in exportProducts)
    if exportCount == 0:
        exportCount = None
    return exportCount


def searchItem(request):

    query = request.GET['q']
    items = Item.objects.filter(name__icontains=query)

    context = {}
    context['items'] = []
    for item in items:
        product = item.product
        product_images = Image.objects.filter(product=product)
        if product_images.count() > 0:
            img = product_images[0].path
        else:
            img = None
        discount_rate = None
        try:
            discount = Discount.objects.get(id=item.id)
            discount_rate = round(
                discount.discount_value / item.price * 100) - 100
        except Discount.DoesNotExist:
            pass

        context['items'].append((item, img, discount_rate))
    context['query'] = query

    return render(request, 'search_item.html', context)

def handleComment(request):
    rate = request.POST['rate']
    item_id = request.POST['item_id']

    # customer
    customer_id = request.session['customer']
    customer = Customer.objects.get(pk=customer_id)

    # comment
    comment = Comment()
    comment.content = request.POST['customer-comment']
    comment.save()

    feedBack = Feedback()
    feedBack.customer = customer
    feedBack.item = Item.objects.get(pk=item_id)
    feedBack.rate_score = rate
    feedBack.comment = comment
    feedBack.isProcessed = False
    feedBack.save()

    return redirect('mystore:item-detail', item_id=item_id)


def getSimilarItem(item_id):

    item = Item.objects.get(pk=item_id)

    typee = Type.objects.get(pk=item.product.type.id)

    products = Product.objects.filter(type=typee)

    items = []
    for product in products:
        try:
            itemm = Item.objects.get(product=product)
            items.append(itemm)
        except Item.DoesNotExist:
            pass
    return [it for it in items if it.id != item.id]


def item_type(request, type_id):
    type = Type.objects.get(id = type_id )
    products = Product.objects.filter(type = type)
    
    items = []
    for product in products:
        try:
            itemm = Item.objects.get(product=product)
            items.append(itemm)
        except Item.DoesNotExist:
            pass
    

    context = {}
    context['items'] = []
    for item in items:
        product = item.product
        product_images = Image.objects.filter(product=product)
        if product_images.count() > 0:
            img = product_images[0].path
        else:
            img = None
        discount_rate = None
        try:
            discount = Discount.objects.get(id=item.id)
            discount_rate = round(
                discount.discount_value / item.price * 100) - 100
        except Discount.DoesNotExist:
            pass

        context['items'].append((item, img, discount_rate))
    context['type'] = type

    return render(request, 'search_item.html', context)