from django.urls import path
from .view import index

app_name = 'mystore'

urlpatterns = [
    path('', index.home, name='home'),
]
