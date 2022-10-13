from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'apellidos', 'correo', 'direccion', 'numero', 'imagen')
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'catNombre', 'created_at', 'updated_at')
        
class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ('id', 'proNombre', 'idCategoria', 'descripcion', 'cantidad', 'precio', 'proImagen', 'created_at', 'updated_at')
        
class CotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = ('id', 'idUsuario', 'descripcion', 'cantidad', 'medioContacto', 'created_at', 'updated_at')
        
class ForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foro
        fields = ('id', 'idUsuario', 'descripcion', 'created_at', 'updated_at')