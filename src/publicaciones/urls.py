from django.urls import path
from . import views

urlpatterns = [
    path('ver-publicaciones/', views.PublicacionesView.as_view(), name='publicaciones')
]


# nuestrapagina/publicacones/ver-publicaciones