from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.
class Usuario(AbstractUser):
    telefono=models.CharField(max_length=50, null=True, blank=True)
    domicilio=models.CharField(max_length=100, null=True, blank=True)
    es_colaborador = models.BooleanField(default=False)


    def __str__(self):
        return self.first_name + " " + self.last_name + f'({self.username})'
    
    def get_absolute_url(self):
        return reverse('publicaciones')