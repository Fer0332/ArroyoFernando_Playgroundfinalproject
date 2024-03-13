from django import forms

class FormularioCreacionTermo(forms.Form):
    marca = forms.CharField(max_length=30)
    capacidad = forms.IntegerField()
    color =forms.CharField(max_length=30)
    linea = forms.CharField(max_length=30)
        