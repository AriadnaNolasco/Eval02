from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions  # Importamos viewsets
from .models import Categoria, Transaccion
from .serializers import CategoriaSerializer, TransaccionSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para proporcionar el CRUD completo para el modelo Categoria.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # O IsAuthenticated


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