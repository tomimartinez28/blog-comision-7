from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registrarse/', views.RegistrarseView.as_view(), name='registrarse'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')

]