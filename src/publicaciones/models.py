from django.db import models
from django.urls import reverse
# Create your models here.

class Publicacion(models.Model):
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField()
    categoria = models.CharField(max_length=50)
    creador = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('publicaciones')