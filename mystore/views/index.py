from django.shortcuts import render
from django.template import Context, context
from ..models import *
from ..views import item as it

def home(request):
    items = Item.objects.all()
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
        discount = None
        try:
            discount = Discount.objects.get(item=item)
            discount_rate = round(discount.discount_value / item.price * 100) - 100
        except Discount.DoesNotExist:
            pass
        
        
        feedbacks = Feedback.objects.filter(item=item)
        fb_count = sum(1 for feedback in feedbacks if feedback.isProcessed == True)
        if fb_count == 0:
            rate_avg = 0
            fb_count = None
        else:
            rate_avg = sum(feedback.rate_score for feedback in feedbacks if feedback.isProcessed == True) / fb_count
        exportCount = it.getExportCount(item)
        context['items'].append((item,img, discount,discount_rate,rate_avg, fb_count, exportCount))
    cont = context['items']
    context['items'].sort(key=lambda x : x[4], reverse=True)
    return render(request, 'home.html',context)