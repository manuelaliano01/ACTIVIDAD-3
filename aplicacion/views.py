from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Almacen, Bebida, Fruta, Verdura
from .forms import *

def home (request):
    return render(request,"aplicacion/index.html")

# Vistas Generales #
def almacen(request):
    productos_almacen = Almacen.objects.all()
    return render(request, "aplicacion/almacen.html", {
        'productos_almacen': productos_almacen})

def bebida (request):
    productos_bebida = Bebida.objects.all()
    return render(request,"aplicacion/bebida.html", {
        'productos_bebida': productos_bebida})

def verdura (request):
    productos_verdura = Verdura.objects.all()
    return render(request,"aplicacion/verdura.html",{
        'productos_verdura': productos_verdura})

def fruta (request):
    productos_fruta = Fruta.objects.all()
    return render(request,"aplicacion/fruta.html",{
        'productos_fruta': productos_fruta}) 

def sobre_nos (request):
    return render(request,"aplicacion/sobre.html")

def all_products (request):
    return render(request,"aplicacion/all_products.html")


#Formulario Almacen#
def almacen_form(request):
    if request.method == "POST":
        form = AlmacenForm(request.POST)
        if form.is_valid():
             almacen_nombre = form.cleaned_data.get("nombre")
             almacen_precio = form.cleaned_data.get("precio")
             almacen_unidad = form.cleaned_data.get("unidad")
             almacen= Almacen(nombre = almacen_nombre, precio = almacen_precio, unidad = almacen_unidad)
             almacen.save()
             productos_almacen = Almacen.objects.all()
             return render(request, "aplicacion/almacen.html", {'productos_almacen': productos_almacen})
    else:
        form = AlmacenForm()

    return render(request, "aplicacion/almacenForm.html", {"form": form})

#Formulario Bebida#
def bebida_form(request):
    if request.method == "POST":
        form = BebidaForm(request.POST)
        if form.is_valid():
             bebida_nombre = form.cleaned_data.get("nombre")
             bebida_precio = form.cleaned_data.get("precio")
             bebida_unidad = form.cleaned_data.get("unidad")
             bebida= Bebida(nombre = bebida_nombre, precio = bebida_precio, unidad = bebida_unidad)
             bebida.save()
             productos_bebida = Bebida.objects.all()
             return render(request, "aplicacion/bebida.html", {'productos_bebida': productos_bebida})
    else:
        form = BebidaForm()

    return render(request, "aplicacion/bebidaForm.html", {"form": form})

#Formulario Verdura#
def verdura_form(request):
    if request.method == "POST":
        form = VerduraForm(request.POST)
        if form.is_valid():
             verdura_nombre = form.cleaned_data.get("nombre")
             verdura_precio = form.cleaned_data.get("precio")
             verdura_unidad = form.cleaned_data.get("unidad")
             verdura= Verdura(nombre = verdura_nombre, precio = verdura_precio, unidad = verdura_unidad)
             verdura.save()
             productos_verdura = Verdura.objects.all()
             return render(request, "aplicacion/verdura.html", {'productos_verdura': productos_verdura})
    else:
        form = VerduraForm()

    return render(request, "aplicacion/verduraForm.html", {"form": form})

## Formulario Fruta##
def fruta_form(request):
    if request.method == "POST":
        form = FrutaForm(request.POST)
        if form.is_valid():
             fruta_nombre = form.cleaned_data.get("nombre")
             fruta_precio = form.cleaned_data.get("precio")
             fruta_unidad = form.cleaned_data.get("unidad")
             fruta= Fruta(nombre = fruta_nombre, precio = fruta_precio, unidad = fruta_unidad)
             fruta.save()
             productos_fruta = Fruta.objects.all()
             return render(request, "aplicacion/fruta.html", {'productos_fruta': productos_fruta})
    else:
        form = FrutaForm()

    return render(request, "aplicacion/frutaForm.html", {"form": form})


def buscarAlmacen(request):
    return render(request, "aplicacion/buscar.html")

def encontrarAlmacen(request):
    patron = request.GET.get("buscar")  
    if patron:
        almacen = Almacen.objects.filter(nombre__icontains=patron)
        productos_almacen = {'productos_almacen': almacen}
    else:
        productos_almacen = {'productos_almacen': Almacen.objects.all()}
        
    return render(request, "aplicacion/almacen.html", productos_almacen)

    

