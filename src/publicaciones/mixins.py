from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Publicacion, Comentario

class ColaboradorMixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        return usuario.es_colaborador or usuario.is_superuser

class CreadorMixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        objeto = self.get_object()

        if isinstance(objeto, Publicacion):
            return usuario == objeto.creador or usuario.is_superuser
        elif isinstance(objeto, Comentario):
            return usuario == objeto.creador or usuario.is_superuser or usuario == objeto.publicacion.creador
        
            