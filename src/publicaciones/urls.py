from django.urls import path
from . import views

urlpatterns = [
    path('ver-publicaciones/', views.PublicacionesView.as_view(), name='publicaciones'),
    path('publicar/', views.Publicar.as_view(), name='publicar'),
    path('modificar/<int:pk>', views.ModificarPublicacionView.as_view(), name='modificar-publicacion'),
    path('eliminar/<int:pk>', views.EliminarPublicacionView.as_view(), name='eliminar-publicacion'),
]


# nuestrapagina/publicacones/ver-publicaciones