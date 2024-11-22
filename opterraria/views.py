from django.shortcuts import render
from django.http import HttpResponse
from .models import Npc
def index(request):
    context={"NPCs":Npc.objects.all()}
    return render(request, template_name="index.html",context=context)
# Create your views here.


def index2(request):
    return HttpResponse("Hola 2")
# Create your views here.


def vida(request):
    return HttpResponse("Vida Hpta")
# Create your views here.