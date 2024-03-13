from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from producto.models import Mate
from django.urls import reverse_lazy

def mates(request):
    ...
class Mates(ListView):
    model = Mate
    context_object_name = "mates"
    template_name = "mates/mates.html"

class CrearMate(CreateView):
    model = Mate
    template_name = "mates/crear_mate.html"
    fields = ["marca", "capacidad", "color", "tipo"]
    success_url = reverse_lazy("mates")
    


