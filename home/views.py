from django.http import HttpResponse
from django.shortcuts import render


def homeview(request):
    return render(request,'home/index.html')

def carritoview(request):
    return render(request,'home/carrito.html')

def pagoview(request):
    return render(request,'home/pago.html')


