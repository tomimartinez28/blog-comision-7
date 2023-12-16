from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Usuario
from .forms import RegistrarseForm, EditarPerfilForm
from django.contrib.auth import login
from django.urls import reverse



# Create your views here.
class RegistrarseView(CreateView):
    model=Usuario
    template_name='usuarios/registrarse.html'
    form_class = RegistrarseForm
 
    def form_valid(self, form):
        response = super().form_valid(form)
        usuario = form.save()
        login(self.request, usuario)
        return response
    
    
def mi_perfil_view(request):
    return render(request, 'usuarios/mi-perfil.html', {})
    

class EditarPerfilView(UpdateView):
    template_name='usuarios/editar-perfil.html'
    model=Usuario
    form_class=EditarPerfilForm

    def get_success_url(self):
        return reverse('mi-perfil')