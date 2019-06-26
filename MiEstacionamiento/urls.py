from django.urls import path,include
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from rest_framework import routers

urlpatterns = [
    path('',views.index,name="index"),
    path('',views.navbar,name="navbar"),
    path('',views.footer,name="footer"),
    path('perfil',views.perfil,name="perfil"),
    path('estacionamientos',views.estacionamientos,name="estacionamientos"),



    #CRUD USUARIOS
    path('crear_U',views.crear_U, name="crear_U"),

    #CRUD VEHICULOS
    path('crear_V',views.crear_V, name="crear_V"),

    #CRUD ESTACIONAMIENTOS
    path('crear_E',views.crear_E, name="crear_E"),

    #CRUD USUARIOS
    path('crear_A',views.crear_A, name="crear_A"),
    

    
]