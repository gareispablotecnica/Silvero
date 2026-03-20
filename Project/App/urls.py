from django.urls import path
# ------> * Todas las Funciones
from .views import *
urlpatterns = [
    # 'url',Funcion,Nombre para HTML
    path('',Home,name='Inicio'),
    path('Productos',Productos,name='Productos'),
]