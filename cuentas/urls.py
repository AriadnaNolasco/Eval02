from rest_framework import routers
from django.urls import path, include
from . import views
from .api import CategoriaViewSet, TransaccionViewSet  # Importamos los ViewSets

app_name = 'cuentas'

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')  # Registramos el ViewSet de Categoria
router.register(r'transacciones', TransaccionViewSet, basename='transaccion')  # Registramos el ViewSet de Transaccion

urlpatterns = [
    path('usuarios/registro/', views.RegistroUsuarioAPIView.as_view(), name='registro_usuario'),
    path('usuarios/login/', views.LoginUsuarioAPIView.as_view(), name='login_usuario'),
    path('', include(router.urls)),  # Incluimos las URLs generadas por el router
]