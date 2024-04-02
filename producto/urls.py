from django.urls import path
from producto import views

urlpatterns = [
    path('mates/', views.Mates.as_view(), name="mates"),
    path('mates/nuevo/', views.CrearMate.as_view(), name="crear_mates"),
    path('mates/nuevo/<int:pk>/', views.DetalleMate.as_view(), name="detalle_mate"),
    path('mates/nuevo/<int:pk>/editar/', views.EditarMate.as_view(), name="editar_mates"),
    path('mates/nuevo/<int:pk>/eliminar/', views.EliminarMate.as_view(), name="eliminar_mates"),
]