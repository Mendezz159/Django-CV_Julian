from django.shortcuts import render, redirect
from .models import Contacto, Videojuego
from .forms import CrearRegistroContacto

# Create your views here.
def index(request):
    return render(request, "index.html")

def contactame(request):
    if request.method == 'GET':
        return render(request, "contactame.html", {
            'form': CrearRegistroContacto()
        })
    else:
        Contacto.objects.create(
            nombre=request.POST['nombre'],
            email=request.POST['email'],
            mensaje=request.POST['mensaje']
        )
        return redirect('/')

def open_view(request):
    videojuegos = Videojuego.objects.all()
    return render(request, "open.html", {"videojuegos": videojuegos})