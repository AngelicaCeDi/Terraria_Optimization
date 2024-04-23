from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hola mundo mundial!!!</h1>")
# Create your views here.


def index2(request):
    return HttpResponse("Hola 2")
# Create your views here.


def vida(request):
    return HttpResponse("Vida Hpta")
# Create your views here.