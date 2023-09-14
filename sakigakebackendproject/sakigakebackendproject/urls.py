from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="MzaziConnect API",
        default_version='v1',
        description="MzaziConnect assignment and shops models endpoints",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
=======
from django.urls import path, re_path, include
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
        description="MzaziConnect students and parents models endpoints",
        description="MzaziConnect parents and teacher comment model",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),

>>>>>>> b8cca4b474e0a221d6680d1b42df7e35686a365f
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
<<<<<<< HEAD


urlpatterns = [
    path('admin/', admin.site.urls),
    path('assignment/', include('assignment.urls')),
    path('shop/', include('shop.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
=======

urlpatterns = [
    path('admin/', admin.site.urls),
    path("school/" , include("school.urls")),

    path('teachers/', include('teachers.urls')),
    path('subjects/', include('subjects.urls')),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0),name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'),
    path("comments/", include ("comments.urls")),
    path("accounts/", include ("accounts.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
>>>>>>> b8cca4b474e0a221d6680d1b42df7e35686a365f
