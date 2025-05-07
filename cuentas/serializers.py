from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Categoria, Transaccion

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = ['id','tipo', 'monto', 'fecha', 'categoria', 'descripcion']

class CategoriaSerializer(serializers.ModelSerializer):
    transacciones = TransaccionSerializer(many=True, read_only=True)
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'transacciones']

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