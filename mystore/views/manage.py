from django.shortcuts import render

def saler(request):
    return render(request, 'manager/saler.html')

def shipment(request):
    return render(request, 'manager/shipment.html')

def newProduct(request):
    return render(request, 'manager/new-product.html')

def newBookDetail(request):
    return render(request, 'manager/new-book-detail.html')

def newElectroDetail(request):
    return render(request, 'manager/new-electro-detail.html')

def newClothesDetail(request):
    return render(request, 'manager/new-clothes-detail.html')