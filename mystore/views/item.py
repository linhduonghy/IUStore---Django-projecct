from django.shortcuts import render


def showItemDetail(request, item_id):
    return render(request, "item_detail.html")


def searchItem(request):

    query = request.GET['q']
    # get list product relevance
    return render(request, 'search_item.html')
