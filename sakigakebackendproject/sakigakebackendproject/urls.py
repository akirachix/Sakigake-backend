from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(

        title="Teacher and subject API",
        default_version='v1',
        description="MzaziConnect pateachers and subject teachers",
        contact=openapi.Contact(email="soniauwamahooro@gmail.com"),

        title="MzaziConnect API",
        default_version='v1',
        description="MzaziConnect parents and teacher comment model",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('teachers/', include('teachers.urls')),
    path('subjects/', include('subjects.urls')),

    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]

    path("comments/", include ("comments.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


]

