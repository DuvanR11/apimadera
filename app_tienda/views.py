from rest_framework import generics
from .models import *
from . serializers import *
# Create your views here.

# ------------------USUARIO----------------
class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# --------------CATEGORIA-----------------------
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
# --------------PRODUCTOS-----------------------
class ProductosList(generics.ListCreateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    

class ProductosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    
# --------------COTIZACIÓN-----------------------
class CotizacionList(generics.ListCreateAPIView):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer
    

class CotizacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer
    
    
# --------------FORO-----------------------
class ForoList(generics.ListCreateAPIView):
    queryset = Foro.objects.all()
    serializer_class = ForoSerializer
    

class ForoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foro.objects.all()
    serializer_class = ForoSerializer