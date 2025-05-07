from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Categoria, Transaccion, Cuenta, Presupuesto
from django.contrib.auth import get_user_model

class TransaccionSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), default=serializers.CurrentUserDefault())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    cuenta = serializers.PrimaryKeyRelatedField(queryset=Cuenta.objects.all())

    class Meta:
        model = Transaccion
        fields = ['id', 'usuario', 'tipo', 'monto', 'fecha', 'categoria', 'cuenta', 'descripcion']
        read_only_fields = ['id', 'usuario']

class CategoriaSerializer(serializers.ModelSerializer):
    transacciones = TransaccionSerializer(many=True, read_only=True)
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'transacciones']

class CuentaSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = Cuenta
        fields = ['id', 'usuario', 'nombre', 'saldo', 'moneda', 'fecha_creacion']
        read_only_fields = ['id', 'fecha_creacion']

class PresupuestoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), default=serializers.CurrentUserDefault())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())

    class Meta:
        model = Presupuesto
        fields = ['id', 'usuario', 'categoria', 'monto_presupuestado', 'periodo_inicio', 'periodo_fin']
        read_only_fields = ['id', 'usuario']
        
class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Los passwords no coinciden."})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})