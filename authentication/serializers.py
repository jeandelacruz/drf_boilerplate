from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed, NotFound
from rest_framework_simplejwt.tokens import RefreshToken
from secrets import token_hex
from .utils.mailing import Mailing


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
    username = serializers.CharField(
        min_length=3, max_length=150, write_only=True
    )
    password = serializers.CharField(max_length=12, write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        username = obj.get('username')
        password = obj.get('password')

        user = authenticate(username=username, password=password)
        jwt = RefreshToken.for_user(user)

        return {
            'access_token': str(jwt.access_token),
            'refresh_token': str(jwt)
        }

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


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    message = serializers.ReadOnlyField()

    def validate(self, attrs):
        email = attrs.get('email')
        if not User.objects.filter(email=email).exists():
            raise NotFound('User not found, retry to other email')
        return attrs

    def create(self, validated_data):
        email = validated_data.get('email')
        new_password = token_hex(5)
        mailing = Mailing()

        record = User.objects.filter(email=email).first()
        record.set_password(new_password)
        record.save()

        mailing.email_reset_password(
            recipient=email,
            name=record.first_name,
            password=new_password
        )

        validated_data['message'] = 'Send mail to new password'
        return validated_data
