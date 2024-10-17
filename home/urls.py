from django.urls import path
from .views import homeview
from .views import carritoview, pagoview

urlpatterns = [
    path('',homeview, name='home'),
    path('carritoview', carritoview, name='carritoview'), 
    path('pago/', pagoview, name='home') 
]





