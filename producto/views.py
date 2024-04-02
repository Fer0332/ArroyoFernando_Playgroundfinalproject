from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from producto.models import Mate
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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

class EliminarMate(LoginRequiredMixin, DeleteView):
    model = Mate
    template_name = "mates/eliminar_mates.html"
    success_url = reverse_lazy("mates")
    
class EditarMate(LoginRequiredMixin, UpdateView):
    model = Mate
    template_name = "mates/editar_mate.html"
    success_url = reverse_lazy("mates")
    fields = ["marca", "capacidad", "color", "tipo"]

class DetalleMate(DetailView):
    model = Mate
    template_name = "mates/detalle_mate.html"
    


