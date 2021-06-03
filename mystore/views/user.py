from django.shortcuts import redirect, render
from django.template import Context, context
from . import index

def login(request):
    
    if request.method == 'GET':
        a = request.META.get('HTTP_REFERER')
        
        return render(request, 'user/login.html')

    if request.method == 'POST':
        usn = request.POST.get('username')
        request.session['user'] = usn
        return redirect('mystore:home')


def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('mystore:home')

def register(request):
    return render(request, 'user/register.html')