from django import forms
from .models import Publicacion, Comentario


class PublicarForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'cuerpo', 'categoria', 'imagen']


class ComentarioForm(forms.ModelForm):
    class Meta:
        model=Comentario
        fields=['texto']
        labels = {
            'texto' : '',
        }