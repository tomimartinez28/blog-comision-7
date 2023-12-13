from typing import Any
from django.shortcuts import render, redirect
from .models import Publicacion, Comentario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse
from .forms import PublicarForm, ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import ColaboradorMixin, CreadorMixin

""" # View basada en funcion, para enlistar las publicaciones.
def publicaciones_view(request):
    ctx = {
        'publicaciones' : Publicacion.objects.all(),
    }
    return render(request, 'publicaciones.html', ctx)
  """

# View basada en clase, para enlistar las publicaciones.
class PublicacionesView(ListView):
    template_name = 'publicaciones/publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'
    

# View basada en funcion para CREAR una publicacion.
""" 
def publicar_view(request):
    if request.method == 'POST':
        form = PublicarForm(request.POST)
        if form.is_valid():
            nueva_publicacion = form.save()
            return redirect('publicaciones')
    else:
        form = PublicarForm()
        ctx = {'form' : form}
        return render(request, 'publicaciones/publicar.html', ctx)


 """

# View basada en clase para CREAR una publicacion.
class Publicar(LoginRequiredMixin, ColaboradorMixin, CreateView):
    model = Publicacion
    template_name = 'publicaciones/publicar.html'
    form_class = PublicarForm

    def form_valid(self, form):
        f = form.save(commit=False) # aca le paro el carro al formulario para que no guarde
        f.creador_id = self.request.user.id
        return super().form_valid(f)
    

    def get_success_url(self):
        return reverse('publicaciones')


# # View basada en clase para MODIFICAR una publicacion.
class ModificarPublicacionView(LoginRequiredMixin, CreadorMixin, UpdateView):
    model = Publicacion
    template_name = 'publicaciones/modificar-publicacion.html'
    form_class = PublicarForm
    success_url = '../ver-publicaciones/'


# View basada en clase para ELIMINAR una publicacion.
class EliminarPublicacionView(LoginRequiredMixin, CreadorMixin, DeleteView):
    model=Publicacion
    template_name='publicaciones/eliminar-publicacion.html'
    success_url = '../ver-publicaciones/'


# View para ver en detalle UNA publicacion

class DetallePublicacion(DetailView):
    model=Publicacion
    template_name = 'publicaciones/detalle.html'
    context_object_name = 'publicacion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        return context


    def post(self, request, *args, **kwargs):
        
        if not self.request.user.is_authenticated:
            return redirect('login')

        publicacion = self.get_object()
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.creador_id = self.request.user.id
            comentario.publicacion = publicacion
            comentario.save()
            return super().get(request)
        else:
            return super().get(request)



class BorrarComentarioView(LoginRequiredMixin, CreadorMixin, DeleteView):
    template_name='comentarios/borrar-comentario.html'
    model=Comentario

    def get_success_url(self):
        return reverse('detalle-publicacion', args=[self.object.publicacion.id])
    
class EditarComentarioView(LoginRequiredMixin, CreadorMixin, UpdateView):
    template_name='comentarios/editar-comentario.html'
    model=Comentario
    form_class = ComentarioForm

    def get_success_url(self):
        return reverse('detalle-publicacion', args=[self.object.publicacion.id])