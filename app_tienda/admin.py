from django.contrib import admin
from .models import *

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_filter = ['apellidos']
    list_display = [ 'username']
    search_fields = [ 'username']
    list_per_page: 12
    
class CategoriasAdmin(admin.ModelAdmin):
    list_filter = ['catNombre']
    list_display = [ 'catNombre', 'created_at', 'updated_at']
    search_fields = [ 'catNombre','created_at', 'updated_at'    ]
    list_per_page: 12

class ProductosAdmin(admin.ModelAdmin):
    list_filter = ['idCategoria']
    list_display = [ 'proNombre', 'idCategoria',  'descripcion', 'cantidad','precio', 'proImagen', 'created_at', 'updated_at']
    search_fields = [ 'proNombre', 'idCategoria',  'descripcion', 'cantidad','precio', 'proImagen', 'created_at', 'updated_at']
    list_per_page: 12
    

class CotizacionAdmin(admin.ModelAdmin):
    list_filter = ['medioContacto']
    list_display = [ 'idUsuario', 'descripcion',  'cantidad', 'medioContacto','created_at', 'updated_at']
    search_fields = [ 'idUsuario', 'descripcion',  'cantidad', 'medioContacto','created_at', 'updated_at'    ]
    list_per_page: 12

class ForoAdmin(admin.ModelAdmin):
    list_filter = ['created_at']
    list_display = [ 'idUsuario', 'descripcion', 'created_at', 'updated_at']
    search_fields = [ 'idUsuario', 'descripcion', 'created_at', 'updated_at'    ]
    list_per_page: 12

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Categoria, CategoriasAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Cotizacion, CotizacionAdmin)
admin.site.register(Foro, ForoAdmin)
