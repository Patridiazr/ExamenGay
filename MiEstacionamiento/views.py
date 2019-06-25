from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Usuario,Vehiculo

# Create your views here.
def index(request):
    return render(request,'index.html')
def navbar(request):
    return render(request,'navbar.html')
def footer (request):
    return render (request,'footer.html')
def perfil (request):
    return render (request,'perfil.html')




#CRUD USUARIOS
def crear_U(request):
    username = request.POST.get('username','')
    first_name = request.POST.get('nombre','')
    last_name = request.POST.get('apellido','')
    email = request.POST.get('email','')
    password = request.POST.get('password','')
    direccion = request.POST.get('direccion','')
    tarjeta = request.POST.get('tarjeta','')
    banco = request.POST.get('banco')
    usuario = Usuario(username=username,first_name=first_name,last_name=last_name,email=email,password=password,direccion=direccion,tarjeta=tarjeta,
    banco=banco)
    usu =User(username=username,password=password)
    usuario.save()
    usu.save()
    return HttpResponse('<script>alert("Cliente Agregado");'+
                        ' window.location.href="/";</script>')


#CRUD VEHICULOS
def crear_v(request):
    patente = request.POST.get('patente')
    marca = request.POST.get('marca')
    modelo = request.POST.get('modelo')
    año = request.POST.get('año')
    vehiculo = Vehiculo(patente=patente,marca=marca,modelo=modelo,año=año)
    vehiculo.save()
    return HttpResponse('<script>alert("Vehiculo registrado");'+
                        ' window.location.href="/";</script>')

#LOGIN
def login_iniciar(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    print(username, password)
    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto.");'+
                            ' window.location.href="/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); ' +
                            'window.location.href="/";</script>')

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def cerrar_session(request):
    logout(request)
    return HttpResponse('<script>alert("Cierre de sesión correcto.");'+
                        ' window.location.href="/";</script>') 