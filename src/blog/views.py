from django.shortcuts import render
from publicaciones.models import Publicacion

# vista basada en una funcion
def index_view(request):
    ctx = {
        'mejores_posteo' : Publicacion.objects.order_by('-me_gusta')[:1]
    }
    return render(request, 'index.html', ctx)

