from django.shortcuts import render
from .models import Post, Evento
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

#vista basada en clases
class PostListViews(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"

class PostDetailViews(DetailView):
    model = Post
    template_name = "posts/post_individual.html"
    context_object_name = "posts"
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
    model = Post
    template_name = "posts/crear_post.html"
    fields = ["titulo", "subtitulo", "fecha", "texto", "activo", "categoria", "imagen", "publicado"]
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

