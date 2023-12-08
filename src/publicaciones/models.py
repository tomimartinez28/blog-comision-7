from django.db import models
from django.urls import reverse
from usuarios.models import Usuario
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='publicaciones', null=True)
    creador = models.ForeignKey(Usuario, related_name='publicaciones', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('publicaciones')
    


class Comentario(models.Model):
    fecha = models.DateField(auto_now_add=True)
    texto = models.TextField()
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    creador = models.ForeignKey(Usuario, related_name='comentarios', on_delete=models.CASCADE)

    def __str__(self):
        return self.publicacion.titulo + "-" + self.creador.username