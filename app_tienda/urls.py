from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Usuario
    re_path(r'^usuario$', views.UsuarioList.as_view()),
    re_path(r'^usuario/(?P<pk>[0-9]+)$', views.UsuarioDetail.as_view()),
    
    # Categoria
    re_path(r'^categoria$', views.CategoriaList.as_view()),
    re_path(r'^categoria/(?P<pk>[0-9]+)$', views.CategoriaDetail.as_view()),
    
    # Producto
    re_path(r'^producto$', views.ProductosList.as_view()),
    re_path(r'^producto/(?P<pk>[0-9]+)$', views.ProductosDetail.as_view()),
    
    # Cotización
    re_path(r'^cotizacion$', views.CotizacionList.as_view()),
    re_path(r'^cotizacion/(?P<pk>[0-9]+)$', views.CotizacionDetail.as_view()),
    
    # Foro
    re_path(r'^foro$', views.ForoList.as_view()),
    re_path(r'^foro/(?P<pk>[0-9]+)$', views.ForoDetail.as_view()),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)