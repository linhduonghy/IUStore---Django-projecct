from django.shortcuts import redirect, render
from django.template import Context, context
from ..models import *
from ..views import cart

def login(request):

    if request.method == 'GET':
        if 'user' in request.session:
            return redirect('mystore:home')

        return render(request, 'user/login.html')

    if request.method == 'POST':
        usn = request.POST.get('username')
        pwd = request.POST.get('password')
        try:
            user = Account.objects.get(username=usn)
        except Account.DoesNotExist:
            message = "User not exist, please login!!"
            return render(request, 'user/login.html', {"msg_user": message})
        if user.password != pwd:
            message = "Wrong password!!"
            return render(request, 'user/login.html', {"msg_user": message})

        member = Member.objects.get(account=user)
        request.session['user'] = member.name   
        request.session['member'] = member.id

        # customer
        if user.permission.level == 3:
            # set cart for customer
            customer = Customer.objects.get(member=member)
            request.session['customer'] = customer.id
            cart.setCart(request)
            return redirect('mystore:home')
        else:
            return redirect('mystore:saler')


def logout(request):
    if 'user' in request.session:
        del request.session['user']
    if 'customer' in request.session:
        del request.session['customer']
    if 'member' in request.session:
        del request.session['member']
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('mystore:home')


def register(request):
    return render(request, 'user/register.html')