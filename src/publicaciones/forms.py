from django import forms
from .models import Publicacion


class PublicarForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'cuerpo', 'categoria', 'creador']


