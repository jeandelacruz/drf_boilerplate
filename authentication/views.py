from rest_framework.request import Request
from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import RegisterSerializer, LoginSerializer, ResetPasswordSerializer


# Registro - POST -> 201
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    http_method_names = ['post']

    @swagger_auto_schema(
        operation_summary='Endpoint para registrar un usuario',
        operation_description='En este servicio se podra crear un usuario nuevo',
        security=[]
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
        operation_description='En este endpoint puedes logearte con tu usuario y contraseña',
        security=[]
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Refresh Token - POST -> 200
class RefreshTokenView(TokenViewBase):
    serializer_class = TokenRefreshSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        operation_summary='Endpoint para generar un nuevo access_token',
        operation_description='En este servicio podemos generar un nuevo access_token desde el refresh_token'
    )
    def post(self, request):
        return super().post(request)


# Reinicio Contraseña - POST -> 200
class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    @swagger_auto_schema(
        operation_summary='Endpoint para resetear la contraseña',
        operation_description='En este servicio podemos reiniciar la contraseña y a su vez que nos llegue un correo con la nueva',
        security=[]
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
