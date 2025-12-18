from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from .forms import RegistroUsuarioForm



class LoginUsuarioView(LoginView):
    template_name = "usuario/login.html"
    success_url = reverse_lazy("post:index") 


class LogoutUsuarioView(LogoutView):
    next_page = reverse_lazy("inicio")

class PerfilUsuarioView(LoginRequiredMixin, TemplateView):
    template_name = "usuario/perfil.html"
    
class RegistroUsuarioView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = "usuario/registro.html"
    success_url = reverse_lazy("usuario:login")

    def form_valid(self, form):
        messages.success(self.request, "Usuario creado correctamente. Iniciar sesión.")
        return super().form_valid(form)