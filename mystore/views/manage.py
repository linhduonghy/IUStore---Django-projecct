from django.shortcuts import render
from ..models import *

def saler(request):
    return render(request, 'manager/saler.html')

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
    
    typee = Type.objects.get(pk=type_id)
    # attributes of product type
    typeAttributes = AttributeType.objects.filter(type=typee)
    context = {}
    context['attributes'] = typeAttributes
    
    # all warehouses
    warehouses = Warehouse.objects.all()
    context['warehouses'] = warehouses
    return render(request, template_name='manager/new-clothes-product.html', context=context)

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