from django.urls import path

from inicio.views import inicio, mostrar_horario, saludos

urlpatterns = [
    path('', inicio, name="inicio"),
    path('mostrar-horario/', mostrar_horario, name="mostrar_horario"),
    path('saludos/<str:nombre>/<str:apellido>/', saludos, name="saludos"), 
        
]
