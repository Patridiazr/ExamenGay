from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from Usuarios.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Usuario,Vehiculo,Estacionamiento,Arrendador

# Create your views here.
def index(request):
    return render(request,'index.html')
def navbar(request):
    return render(request,'navbar.html')
def footer (request):
    return render (request,'footer.html')
def perfil (request):
    vehiculo = Vehiculo.objects.all()
    estacionamiento = Estacionamiento.objects.all()
    cliente = Usuario.objects.all()
    arrendador = Arrendador.objects.all()
    contexto = {'cliente':cliente,'arrendador':arrendador,'vehiculo':vehiculo,'estacionamiento':estacionamiento}
    return render (request,'perfil.html',contexto)
def estacionamientos (request):
    estacion = Estacionamiento.objects.all()
    contexto = {'estacion':estacion}
    return render (request,'estacionamientos.html',contexto)




#CRUD USUARIOS
def crear_U(request):
    rut = request.POST.get('rut')
    first_name = request.POST.get('first_name','')
    last_name = request.POST.get('last_name','')
    correo = request.POST.get('correo','')
    contra = request.POST.get('contra','')
    direccion = request.POST.get('direccion','')
    tarjeta = request.POST.get('tarjeta','')
    banco = request.POST.get('banco')
    usuario = Usuario(rut=rut,first_name=first_name,last_name=last_name,correo=correo,contra=contra,direccion=direccion,tarjeta=tarjeta,
    banco=banco)
    usu = User.objects.create_user(email=correo,password=contra,tipo="cliente")
    usuario.save()
    usu.save()
    return HttpResponse('<script>alert("Dueño Agregado");'+
                        ' window.location.href="/";</script>')


#CRUD VEHICULOS
def crear_V(request):
    rut = request.POST.get('rut')
    patente = request.POST.get('patente')
    marca = request.POST.get('marca')
    modelo = request.POST.get('modelo')
    año = request.POST.get('año')
    vehiculo = Vehiculo(rut=rut,patente=patente,marca=marca,modelo=modelo,año=año)
    vehiculo.save()
    return HttpResponse('<script>alert("Vehiculo registrado");'+
                        ' window.location.href="/";</script>')


#CRUD ESTACIONAMIENTOS
def crear_E(request):
    rut = request.POST.get('rut')
    direccion = request.POST.get('direccion')
    comuna = request.POST.get('comuna')
    valor = request.POST.get('valor')
    estacionamiento = Estacionamiento(rut=rut,direccion=direccion,comuna=comuna,valor=valor)
    estacionamiento.save()
    return HttpResponse('<script>alert("Estacionamiento registrado");'+
                        ' window.location.href="/";</script>')



#CRUD USUARIOS ARRENDADOR
def crear_A(request):
    rut = request.POST.get('rut')
    first_name = request.POST.get('first_name','')
    last_name = request.POST.get('last_name','')
    correo = request.POST.get('correo','')
    contra = request.POST.get('contra','')
    direccion = request.POST.get('direccion','')
    tarjeta = request.POST.get('tarjeta','')
    banco = request.POST.get('banco')
    usuario = Arrendador(rut=rut,first_name=first_name,last_name=last_name,correo=correo,contra=contra,direccion=direccion,tarjeta=tarjeta,
    banco=banco)
    usu = User.objects.create_user(email=correo,password=contra,tipo="arrendador")
    usuario.save()
    usu.save()
    return HttpResponse('<script>alert("Arrendador Agregado");'+
                        ' window.location.href="/";</script>')