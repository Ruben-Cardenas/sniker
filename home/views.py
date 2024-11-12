from django.http import HttpResponse
from django.shortcuts import render


def homeview(request):
    return render(request,'home/index.html')

def carritoview(request):
    return render(request,'home/carrito.html')

def pagoview(request):
    return render(request,'home/pago.html')

def secionview(request):
    return render(request,'home/secion.html')

def adminview(request):
    return render(request,'home/admin.html')

def crud_tiendaview(request):
    return render(request,'home/crud_tienda')
