from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import RegistroSerializer, LoginSerializer

class RegistroUsuarioAPIView(generics.CreateAPIView):
    """
    Vista para registrar nuevos usuarios.
    """
    queryset = User.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [permissions.AllowAny]  # Cualquiera puede registrarse

class LoginUsuarioAPIView(generics.CreateAPIView):
    """
    Vista para el inicio de sesión de usuarios.
    """
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]  # Cualquiera puede intentar iniciar sesión

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])
        if user:
            return Response({'token': user.auth_token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        
