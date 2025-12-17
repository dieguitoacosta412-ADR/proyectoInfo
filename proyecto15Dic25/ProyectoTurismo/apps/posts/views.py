from django.shortcuts import render
from .models import Post, Evento
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import CrearPost

#vista basada en clases
class PostListViews(ListView):
    model = Post
    template_name = "posts/post.html"
    context_object_name = "post"

class PostDetailViews(DetailView):
    model = Post
    template_name = "posts/post_individual.html"
    context_object_name = "post"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()

class EventoViews(ListView):
    model = Evento
    template_name = "posts/eventos.html"
    context_object_name = "eventos"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()

class EventoDetailViews(DetailView):
    model = Evento
    template_name = "posts/post_individual.html"
    context_object_name = "evento"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()
    
class CrearPostView(LoginRequiredMixin, CreateView):
    model = CrearPost
    template_name = "posts/crear_post.html"
    fields = ["titulo", "subtitulo", "texto", "activo", "categoria", "imagen"]
    success_url = reverse_lazy("post")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

