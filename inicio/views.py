from datetime import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import Template, Context, loader   
from inicio.models import termo
from inicio.forms import FormularioCreacionTermo

def inicio(request):
    #V1
    # archivo_abierto= open(r"C:\Users\foarr\OneDrive\Documentos\phyton\ejercicio 2\templates\inicio.html", "r")
    # template= Template(archivo_abierto.read())
    # archivo_abierto.close()
    
    # contexto = Context()
    # template_renderizado = template.render(contexto)
    
    # return HttpResponse(template_renderizado)

    # V2
    # template = loader.get_template("inicio.html")
    # archivo_abierto= open(r"C:\Users\foarr\OneDrive\Documentos\phyton\ejercicio 2\templates\inicio.html", "r")
    # template= Template(archivo_abierto.read())
    # archivo_abierto.close()////// me ahorro todo lo que esta antes con el loader
    
    # contexto = Context() ya no es necesario usar el contexto
    
    dicc = {
        "nombre": "Fernando"
    }
    
    # template_renderizado = template.render(dicc)
    
    # return HttpResponse(template_renderizado)

    #V3
    return render(request, "inicio.html")

def termos(request):
    termos = termo.objects.all()
    return render(request, "termos.html",{"termos": termos})

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
    # return render(request, "crear_termo.html", {})