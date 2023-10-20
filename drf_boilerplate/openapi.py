from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path


views = get_schema_view(
    openapi.Info(
        title='DRF Boilerplate',
        default_version='1.0',
        description='Documentación de los endpoints del boilerplate'
    )
)

urlpatterns = [
    path('swagger-ui/', views.with_ui('swagger'), name='swagger-ui')
]
