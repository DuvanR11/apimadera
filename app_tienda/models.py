from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Usuario(AbstractUser):
    apellidos = models.CharField(max_length=30)
    correo = models.EmailField(max_length=30)
    direccion = models.CharField(max_length=40)
    numero = models.CharField(max_length=40)
    imagen = models.ImageField('foto para tu perfil', upload_to='peril/', blank=True, null=True)

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    catNombre = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.catNombre
    
class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    proNombre = models.CharField(max_length=40)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    proImagen = models.ImageField('foto para tu producto', upload_to='producto/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Cotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    cantidad = models.IntegerField(null=True, blank=True)
    medioContacto = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    
class Foro(models.Model):
    id = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    