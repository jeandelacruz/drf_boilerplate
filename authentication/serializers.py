from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=150)
    email = serializers.EmailField(min_length=6, max_length=160)
    password = serializers.CharField(max_length=12, write_only=True)
    # Campo personalizado
    password_confirmation = serializers.CharField(
        max_length=12, write_only=True
    )

    # Validaciones personalizadas
    # Las validaciones deben estar como un metodo con el prefijo "validate_"
    # Ej: Campo username -> def validate_username(self, value)
    def validate_password_confirmation(self, value):
        data = self.get_initial()
        if value != data.get('password'):
            raise serializers.ValidationError('Password dont match')
        return value

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        return User.objects.create_user(
            **validated_data
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=150)
    password = serializers.CharField(max_length=12)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        # Validar que el usuario exista
        # Validar el hash de la contraseña sea correcta para el usuario
        if not authenticate(username=username, password=password):
            raise AuthenticationFailed(
                'User not found or credentials is invalid'
            )

        return attrs
