from django.shortcuts import render
from .models import Post, Evento
from django.views.generic import ListView, DetailView

# Create your views here.


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

