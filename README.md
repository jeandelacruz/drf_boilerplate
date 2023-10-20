# Boilerplate DRF

---

## Modelos:

- Usuarios (Extender del modelo de Django)

  | campo      | tipo         | constraint |
  | ---------- | ------------ | ---------- |
  | email      | VARCHAR(160) | UNIQUE     |
  | created_at | DATETIME     |            |
  | updated_at | DATETIME     |            |

## Caracteristicas:

1. Login
   - [x] Creación del token de acceso (JWT | access_token - refresh_token)
2. Registro
   - [x] Encriptación de contraseña (pkdpf2)
3. Recuperar Contraseña
   - [x] Generar una nueva contraseña encriptada
   - [x] Enviar un correo con un template (html)
4. CRUD por cada Modelo
   - [x] Listado con paginación
   - [x] Obtener un registro mediante el id
   - [x] Creación de un registro
   - [x] Actualización de un registro
   - [x] Eliminar un registro (SoftDelete)
5. Decoradores
   - [x] Proteger las rutas mediante autenticación
   - [x] Proteger las rutas por rol
6. Documentación y validaciones
   - [x] Swagger OpenAPI
7. Despliegue
   - [x] Render

## PIP

```ssh
pip install Django psycopg2-binary python-decouple
```

## Enviroments

```py
DEBUG=True

DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''
```

## Documentación

- Django Users Model
  - [Extender el modelo de Usuarios](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model)
- ORM
  - [Tipos de datos](https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types)

## Comandos

### Django

1º Crear un proyecto de Django

```sh
django-admin startproject <nombre_proyecto> .
```

2º Iniciar un proyecto de Django

```sh
python manage.py runserver
```

3º Crear super usuario

```sh
python manage.py createsuperuser
```

4º Crear una app

```sh
python manage.py startapp <nombre_app>
```

5º Crear las migraciones

```sh
python manage.py makemigrations
python manage.py makemigrations <nombre_app>
```

6º Sincronizar migraciones

```sh
python manage.py migrate
```
