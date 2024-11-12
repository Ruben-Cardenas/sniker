from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User

# models.py en la aplicación home

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


# models.py en la aplicación home

from django.conf import settings
from django.db import models

class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# models.py en la aplicación home

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en el carrito de {self.carrito.usuario.username}"


class Rol(models.TextChoices):
    CLIENTE = 'Cliente', 'Cliente'
    ADMINISTRADOR = 'Administrador', 'Administrador'

# Definición del modelo Usuario heredando de AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'  # Make email the unique identifier for authentication
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # List the fields you need here

    def __str__(self):
        return self.username


from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields here if needed
    pass
