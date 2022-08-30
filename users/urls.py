"""Define los URL patterns para users"""
from django.urls import path, include
from . import views

app_name = "users"
urlpatterns = [
    # incluimos default auth urls
    path("", include("django.contrib.auth.urls")),
    # Pagina de registro
    path("register/", views.register, name="register"),
]
