from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import RegisterSerializer, LoginSerializer


# Registro - POST -> 201
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    http_method_names = ['post']

    @swagger_auto_schema(
        operation_summary='Endpoint para registrar un usuario',
        operation_description='En este servicio se podra crear un usuario nuevo'
    )
    def post(self, request):
        # instanciar el serializador con los datos del body request
        serializer = self.serializer_class(data=request.data)
        # iniciamos la validación del serializador
        serializer.is_valid(raise_exception=True)
        # ejecutamos la acción
        serializer.save()
        # retornamos la respuesta
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Login - POST -> 200
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    http_method_names = ['post']

    @swagger_auto_schema(
        operation_summary='Endpoint para logearse',
        operation_description='En este endpoint puedes logearte con tu usuario y contraseña'
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Refresh Token - POST -> 200
# Reinicio Contraseña - POST -> 200
