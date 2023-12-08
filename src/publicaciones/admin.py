from django.contrib import admin
from .models import Publicacion, Categoria, Comentario
# Register your models here.

admin.site.register(Publicacion)
admin.site.register(Categoria)
admin.site.register(Comentario)