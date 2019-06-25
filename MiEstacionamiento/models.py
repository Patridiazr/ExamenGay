from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(default="default" ,max_length=20)
    last_name = models.CharField(default="default" ,max_length=20)
    email = models.EmailField( default="default" ,max_length=20)
    password = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    tarjeta = models.IntegerField(default="0")
    banco = models.CharField(max_length=20)

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6)
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=10)
    año = models.IntegerField(default="null")
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)



