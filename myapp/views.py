from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(request):
    return HttpResponse("holis")

def categoria(request):
    return HttpResponse("Categorias")

def login(request):
    return HttpResponse("registro")