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



    #CRUD USUARIOS
    path('crear_U',views.crear_U, name="crear_U"),

    #CRUD VEHICULOS
    

    #LOGIN
    path('login_iniciar',views.login_iniciar, name="login_iniciar"),
    path('cerrarsesion', views.cerrar_session, name="cerrar_session"),


]