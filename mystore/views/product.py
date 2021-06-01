from django.shortcuts import render


def showProductDetail(request, product_id):
    return render(request, "product_detail.html")


def searchProduct(request):

    query = request.GET['q']
    # get list product relevance
    return render(request, 'search_product.html')
