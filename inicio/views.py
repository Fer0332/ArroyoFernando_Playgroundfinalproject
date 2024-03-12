from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader   


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
    
    return render(request, "inicio.html",dicc)

def mostrar_horario(request):
    fecha= datetime.now()
    return HttpResponse(f"Esta es la fecha y hora actual: {fecha}")

def saludos(request, nombre, apellido):
    nombre_formateado= nombre.title()
    apellido_formateado= apellido.title()
    return HttpResponse(f"Bien venido {nombre_formateado} {apellido_formateado}")
