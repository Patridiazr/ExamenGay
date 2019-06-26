from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.IntegerField(default="0")
    first_name = models.CharField(default="default" ,max_length=20)
    last_name = models.CharField(default="default" ,max_length=20)
    correo = models.EmailField( default="default" ,max_length=20)
    contra = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    tarjeta = models.IntegerField(default="0")
    banco = models.CharField(max_length=20)

class Vehiculo(models.Model):
    rut = models.IntegerField(default="0")
    patente = models.CharField(max_length=6)
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=10)
    año = models.IntegerField(default="null")

class Estacionamiento(models.Model):
    rut = models.IntegerField(default="0")
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    valor = models.IntegerField(default="0")

class Arrendador(models.Model):
    rut = models.IntegerField(default="0")
    first_name = models.CharField(default="default" ,max_length=20)
    last_name = models.CharField(default="default" ,max_length=20)
    correo = models.EmailField( default="default" ,max_length=20)
    contra = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    tarjeta = models.IntegerField(default="0")
    banco = models.CharField(max_length=20)



