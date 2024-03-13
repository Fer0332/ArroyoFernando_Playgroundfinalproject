from django.urls import path
from producto import views

urlpatterns = [
    path('mates/', views.Mates.as_view(), name="mates"),
    path('mates/nuevo/', views.CrearMate.as_view(), name="crear_mates"),
]