from django.urls import path

from inicio.views import crear_termo, inicio, mostrar_horario, saludos
from .views import termos, ver_termo, eliminar_termo, editar_termo


# urlpatterns = [
#     path('', inicio, name="inicio"),
#     path('mostrar-horario/', mostrar_horario, name="mostrar_horario"),
#     path('saludos/<str:nombre>/<str:apellido>/', saludos, name="saludos"), 
#     path("termos/", termos, name="termos"),
#     path('termos/nuevo/<str:marca>/<int:capacidad>/<str:color>/<str:linea>/', crear_termo, name="crear_termo"),
   
# ]

urlpatterns = [
    path('', inicio, name="inicio"),
    path('mostrar-horario/', mostrar_horario, name="mostrar_horario"),
    path('saludos/<str:nombre>/<str:apellido>/', saludos, name="saludos"), 
    path('termos/', termos, name="termos"),  # Moviendo esta línea antes del patrón más específico
    path('termos/nuevo/', crear_termo, name="crear_termo"),
    path('termos/<int:id_termo>/', ver_termo, name="ver_termo"),
    path('termos/<int:id_termo>/eliminar/', eliminar_termo, name="eliminar_termo"),
    path('termos/<int:id_termo>/editar/', editar_termo, name="editar_termo"),
    # path('termos/nuevo/<str:marca>/<int:capacidad>/<str:color>/<str:linea>/', crear_termo, name="crear_termo"),
]