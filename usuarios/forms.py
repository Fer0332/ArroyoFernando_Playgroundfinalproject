from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.contrib.auth.models import User

class CreacionDeUsuario(UserCreationForm):
    username = forms.CharField(help_text='')
    email = forms.EmailField(help_text="")
    password1 = forms.CharField(label="contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contrasenia", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {llave: "" for llave in fields} 


class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label="Editar la dirección de correo")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    avatar= forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name","avatar"]