from datetime import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import Template, Context, loader   
from inicio.models import termo
from inicio.forms import FormularioCreacionTermo, FormularioBusquedaTermo, FormularioEdicionTermo
from django.contrib.auth.decorators import login_required

def inicio(request):

    
    dicc = {
        "nombre": "Fernando"
    }
    
    # template_renderizado = template.render(dicc)
    
    # return HttpResponse(template_renderizado)

    #V3
    # return render(request, "inicio.html")
    return render(request, "inicio.html")

def termos(request):
    formulario= FormularioBusquedaTermo(request.GET)
    if formulario.is_valid():
        info_busqueda = formulario.cleaned_data.get("marca")
        termos = termo.objects.filter(marca__icontains= info_busqueda)
        
    termos = termo.objects.all()
    return render(request, "termos.html",{"termos": termos,"formulario": formulario})

def mostrar_horario(request):
    fecha= datetime.now()
    return HttpResponse(f"Esta es la fecha y hora actual: {fecha}")

def saludos(request, nombre, apellido):
    nombre_formateado= nombre.title()
    apellido_formateado= apellido.title()
    return HttpResponse(f"Bien venido {nombre_formateado} {apellido_formateado}")

# def crear_termo(request, marca, capacidad, color, linea):
#     Termo = termo(marca= marca, capacidad = capacidad, color= color, linea= linea )
#     Termo.save()
#     return render(request, "crear_termo.html", {"termo": Termo})

def crear_termo(request):
    # print(request.POST)
    # print(request.GET)
    
    
        # if request.method == "POST":
        #v1
        # marca = request.POST.get("marca")
        # capacidad = request.POST.get("capacidad")
        # color = request.POST.get("color")
        # linea = request.POST.get("linea")
        
        # Termo = termo(marca= marca, capacidad = capacidad, color= color, linea= linea )
        # Termo.save()
    formulario = FormularioCreacionTermo()
    if request.method == "POST":
        formulario = FormularioCreacionTermo(request.POST)
        if formulario.is_valid():
            marca = formulario.cleaned_data.get("marca")
            capacidad = formulario.cleaned_data.get("capacidad")
            color = formulario.cleaned_data.get("color")
            linea = formulario.cleaned_data.get("linea")
            
            Termo = termo(marca= marca, capacidad = capacidad, color= color, linea= linea )
            Termo.save()
            return redirect("termos")   
    return render(request, "crear_termo.html", {"formulario": formulario})
    # return render(request, "crear_termo.html", {})inicio/templates/inicio
    
@login_required
def eliminar_termo(request, id_termo):
    termo_obj = termo.objects.get(id= id_termo)
    termo_obj.delete()
    return redirect("termos")
    
@login_required   
def editar_termo(request,id_termo):
    termo_obj = termo.objects.get(id= id_termo)
    formulario = FormularioEdicionTermo(initial={"marca":termo_obj.marca,"capacidad": termo_obj.capacidad ,"color":termo_obj.color,"linea":termo_obj.linea})
    if request.method == "POST":
        formulario = FormularioEdicionTermo(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            termo_obj.marca = info_nueva.get("marca")
            termo_obj.capacidad = info_nueva.get("capacidad")
            termo_obj.color = info_nueva.get("color")
            termo_obj.linea = info_nueva.get("linea")
            
            termo_obj.save()
            
            return redirect("termos")
        
    return render(request,"inicio/editar_termo.html",{"termo": termo_obj, "formulario": formulario} )

def ver_termo(request, id_termo):
    termo_obj = termo.objects.get(id= id_termo)
    return render(request, "inicio/ver_termo.html",{"termo": termo_obj})