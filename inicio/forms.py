from django import forms

class FormularioBaseTermo(forms.Form):
    marca = forms.CharField(max_length=30)
    capacidad = forms.IntegerField()
    color =forms.CharField(max_length=30)
    linea = forms.CharField(max_length=30)
        
class FormularioCreacionTermo(FormularioBaseTermo):
    pass
class FormularioEdicionTermo(FormularioBaseTermo): 
    nota = forms.IntegerField()   
   
    
class FormularioBusquedaTermo(forms.Form):
    marca = forms.CharField(max_length=30,required= False)
        