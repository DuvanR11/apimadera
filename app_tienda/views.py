from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
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

class FiltroProductos(generics.ListCreateAPIView):
    model = Productos
    serializer_class = ProductosSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(idCategoria=self.kwargs['pk'])

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