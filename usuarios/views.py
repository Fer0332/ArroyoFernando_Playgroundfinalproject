from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import CreacionDeUsuario, EditarPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtras


def login(request):
    formulario = AuthenticationForm()
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario= formulario.cleaned_data.get("username")
            contrasenia= formulario.cleaned_data.get("password")
            
            user = authenticate(username= usuario, password= contrasenia)
            
            if user is not None:
                django_login(request, user)
                return redirect("inicio")
    
    return render(request, "usuarios/login.html", {"formulario": formulario})

def registro(request):
    formulario = CreacionDeUsuario()
    
    if request.method == "POST":
        formulario = CreacionDeUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
    
    return render(request, "usuarios/registro.html", {"formulario": formulario})

def perfil(request):
    return render(request, "usuarios/perfil.html")


@login_required
def editar_perfil(request):
    user= request.user
    datos_extra, _ = DatosExtras.objects.get_or_create(user=user)
    
    if request.method == "POST":
        formulario = EditarPerfil(request.POST, instance=user)
        # formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            avatar = request.FILES.get("avatar")
            # avatar = formulario.cleaned_data.get("avatar")
            if avatar:
                datos_extra.avatar = avatar
            datos_extra.save()
            formulario.save()
            return redirect("perfil")
    else:
        formulario = EditarPerfil(instance=user, initial={"avatar": datos_extra.avatar})
        # formulario = EditarPerfil(initial={"avatar": datos_extra.avatar}, instance=request.user)
    
    return render(request, "usuarios/editar_perfil.html", {"formulario": formulario})

class EditarContrasenia(PasswordChangeView):
    template_name = "usuarios/cambiar_contrasenia.html"
    success_url = reverse_lazy("perfil")

# @login_required
# def editar_perfil(request):
#     if request.method == "POST":
#         formulario = EditarPerfil(request.POST, instance=request.user)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect("perfil")
#     else:
#         formulario = EditarPerfil(instance=request.user)
    
#     return render(request, "usuarios/editar_perfil.html", {"formulario": formulario})



# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate, login as django_login
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from usuarios.forms import CreacionDeUsuario, EditarPerfil

# def login(request):
#     formulario = AuthenticationForm()
    
#     if request.method == "POST":
#         formulario = AuthenticationForm(request, data=request.POST)
#         if formulario.is_valid():
#             usuario= formulario.cleaned_data.get("username")
#             contrasenia= formulario.cleaned_data.get("password")
            
#             user = authenticate(username= usuario, password= contrasenia)
            
#             django_login(request, user)
            
#             return redirect("inicio")
    
#     return render(request,"usuarios/login.html",{"formulario": formulario})

# def registro(request):
#     formulario = CreacionDeUsuario()
    
#     if request.method == "POST":
#         formulario = CreacionDeUsuario(request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect("login")
    
#     return render(request,"usuarios/registro.html",{"formulario": formulario})

# def perfil(request):
#     return render(request,"usuarios/perfil.html")

# def editar_perfil(request):
#     print("Entrando en la vista editar_perfil")
#     if request.method == "POST":
#         formulario = EditarPerfil(request.POST, instance=request.user)
#         if formulario.is_valid():
#             formulario.save()
#             print("Formulario guardado correctamente")
#             return redirect("perfil")  # Redirigir al usuario a la página de perfil después de guardar
#         else:
#             print("El formulario no es válido")
#     else:
#         formulario = EditarPerfil(instance=request.user)
#     print("Renderizando el formulario de edición de perfil")
#     return render(request, "usuarios/editar_perfil.html", {"formulario": formulario})




# def editar_perfil(request):
#     if request.method == "POST":
#         formulario = EditarPerfil(request.POST, instance=request.user)
#         if formulario.is_valid():
#             formulario.save()
#             print("Formulario guardado correctamente")
#             return redirect("perfil")  # Redirigir al usuario a la página de perfil después de guardar
#     else:
#         formulario = EditarPerfil(instance=request.user)
#     return render(request, "usuarios/editar_perfil.html", {"formulario": formulario})


# def editar_perfil(request):
    
#     if request.method == "POST":
#         formulario = EditarPerfil(request.POST, instance= request.user)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect("perfil") 
#     else:
#         formulario = EditarPerfil(instance= request.user)
#     return render(request,"usuarios/editar_perfil.html",{"formulario": formulario})

# def editar_perfil(request):
#     if request.method == "POST":
#         formulario = EditarPerfil(request.POST, instance=request.user)
#         if formulario.is_valid():
#             formulario.save()
#             print("Formulario guardado correctamente")
#             return redirect("perfil")  # Redirigir al usuario a la página de perfil después de guardar
#         else:
#             print("Formulario no válido")
#     else:
#         formulario = EditarPerfil(instance=request.user)
#     return render(request, "usuarios/editar_perfil.html", {"formulario": formulario})
