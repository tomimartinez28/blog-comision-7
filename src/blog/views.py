from django.shortcuts import render


# vista basada en una funcion
def index_view(request):
    return render(request, 'index.html', {})

