from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required  # Agregado

urlpatterns = [
    path("login/",views.login,name="login"),
    path("logout/",LogoutView.as_view(template_name= "usuarios/logout.html"), name= "logout"),
    path("registro/",views.registro,name="registro"),
    path("perfil/",views.perfil,name="perfil"),
    path("perfil/editar/", login_required(views.editar_perfil), name="editar_perfil"),  # Modificado
    path("perfil/editar/contrasenia7",views.EditarContrasenia.as_view(),name="cambiar_contrasenia"),
    
    
]
