from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("index")

def login(request):
    return HttpResponse("login")

def main(request):
    return HttpResponse("main")

def signup(request):
    return HttpResponse("signup")

def categories(request):
    return HttpResponse("categories")

def animewatch(request):
    return HttpResponse("anime-watch")

def animedetails(request):
    return HttpResponse("anime-details")

def blog(request):
    return HttpResponse("blog")

def blogdetails(request):
    return HttpResponse("blog-details")