from django.shortcuts import render

# Create your views here.
def publicaciones_view(request):
    return render(request, 'publicaciones.html', {})