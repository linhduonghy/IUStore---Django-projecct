from django.shortcuts import render, redirect

def checkout(request):
    if 'user' not in request.session:
        return redirect('mystore:login')
    return render(request, 'checkout.html')