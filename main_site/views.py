import json
from math import prod
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main_site.models import Correo
from os import listdir
from os.path import isfile, join
from .models import Sala, Gabinete, Silla, Comedor, Escritorio, Nino
# Create your views here.

def index(request):
    return render(request, "main_site/index.html")

def contact(request):
    return render(request, "main_site/contact.html")

def story(request):
    return render(request, "main_site/story.html")

def products(request):
    return render(request, "main_site/products.html")

def salas(request):
    products = Sala.objects.all()
    return render(request, "main_site/category.html", {
        "products": products,
        "dir": "salas",
        "title": "Salas"
    })

def gabinetes(request):
    products = Gabinete.objects.all()
    return render(request, "main_site/category.html", {
        "products": products,
        "dir": "gabinetes",
        "title": "Gabinetes"
    })

def cias(request):
    products = Silla.objects.all()
    return render(request, "main_site/category.html", {
        "products": products,
        "dir": "cias",
        "title": "Cias"
    })

def escritorios(request):
    products = Escritorio.objects.all()
    return render(request, "main_site/category.html", {
        "products": products,
        "dir": "escritorios",
        "title": "Escritorios"
    })

def comedor(request):
    products = Comedor.objects.all()
    return render(request, "main_site/category.html", {
        "products": products,
        "dir": "comedor",
        "title": "Comedor"
    })

def ninos(request):
    products = Nino.objects.all()
    return render(request, "main_site/category.html", {
        "products": products,
        "dir": "ninos",
        "title": "Niños"
    })


@csrf_exempt
def emails(request):
    if request.method == "POST":
        data= json.loads(request.body)
        correo = data.get("correo", "")
        email = Correo(correo = correo)
        email.save()
        return JsonResponse({"message": "Email sent successfully."}, status=201)