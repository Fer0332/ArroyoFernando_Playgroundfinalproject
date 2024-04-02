from django.contrib import admin
from .models import DatosExtras

# Register your models here.
@admin.register(DatosExtras)
class DatosExtrasAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar']  # Campos que se mostrarán en la lista de objetos


