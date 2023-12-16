from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class RegistrarseForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'telefono', 'domicilio', 'imagen_perfil']

    
class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'telefono', 'domicilio', 'imagen_perfil']

    