from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # Sobreescribir campos ya existentes
    email = models.EmailField(unique=True)

    # Crear nuevos campos
    # auto_now_add -> inserta la fecha y la hora actual, solo en la creación
    # auto_now -> inserta la fecha y la hora actual, en cada actualización
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    # Metodos unicos en la clase heredada

    # Menciona los campos a validar (requeridos), para la creación desde el
    # UserManager (createsuperuser)
    REQUIRED_FIELDS = ['email', 'password']

    # Metodo instancia (heredada)
    def create_user(self, **kwargs):
        # { 'username': 'username' }
        # username=kwargs['username']
        record = self.model(**kwargs)
        record.set_password(kwargs['password'])
        record.save()
        return record
