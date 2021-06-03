from django.shortcuts import render


def notification(request):
    return render(request, 'customer/notification.html')


def info(request):
    return render(request, 'customer/user-info.html')


def order(request):
    return render(request, 'customer/order.html')
