from django.shortcuts import redirect, render
from django.template import Context, context
from . import index

url = 'http://127.0.0.1:8000'

def login(request):
    
    if request.method == 'GET':
        a = request.META.get('HTTP_REFERER')
        
        return render(request, 'login.html')

    if request.method == 'POST':
        usn = request.POST.get('username')
        request.session['user'] = usn
        return redirect(url+'/mystore/')


def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect(url+'/mystore/')
