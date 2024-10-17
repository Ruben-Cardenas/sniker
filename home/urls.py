from django.urls import path
from .views import homeview
from .views import carritoview, pagoview

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name='homeview'),  # Esta es la vista principal 'home' (el "index")
    path('carrito/', views.carritoview, name='carritoview'),  # Vista para el carrito
    path('pago/', views.pagoview, name='pagoview'),  # Vista para el pago
]





