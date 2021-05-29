from django.shortcuts import render

def showProductDetail(request, product_id):
    print(product_id)
    return render(request, "product_detail.html")