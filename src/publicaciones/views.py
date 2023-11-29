from django.shortcuts import render
from .models import Publicacion
from django.views.generic import ListView

# View basada en funcion, para enlistar las publicaciones.
""" def publicaciones_view(request):
    ctx = {
        'publicaciones' : Publicacion.objects.all(),
    }
    return render(request, 'publicaciones.html', ctx)
 """

# View basada en clase, para enlistar las publicaciones.
class PublicacionesView(ListView):
    template_name = 'publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'
    