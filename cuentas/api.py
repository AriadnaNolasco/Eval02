from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions  # Importamos viewsets
from .models import Categoria, Transaccion, Cuenta, Presupuesto
from .serializers import CategoriaSerializer, TransaccionSerializer, CuentaSerializer, PresupuestoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para proporcionar el CRUD completo para el modelo Categoria.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # O IsAuthenticated

class CuentaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cuenta.objects.filter(usuario=user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class TransaccionViewSet(viewsets.ModelViewSet):
    """
    ViewSet para proporcionar el CRUD completo para el modelo Transaccion.
    """
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Transaccion.objects.filter(usuario=user)
    
class PresupuestoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para proporcionar el CRUD completo para el modelo Presupuesto.
    """
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Presupuesto.objects.filter(usuario=user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)