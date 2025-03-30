# /home/kali/Documents/paginaWeb/miapp/urls.py
from django.urls import path
from .views import crear_usuario

urlpatterns = [
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
]
