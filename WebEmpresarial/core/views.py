from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("core/Inicio.html")

def about(request):
    return HttpResponse("core/Historia.html")

def services(request):
    return HttpResponse("core/Servicios.html")

def store(request):
    return HttpResponse("core/Visítanos.html")

def contact(request):
    return HttpResponse("core/Contacto.html")

def blog(request):
    return HttpResponse("core/Blog.html")

def sample(request):
    return HttpResponse("core/Sample.html")