from django.urls import path
from .views import PostListViews, PostDetailViews, EventoViews, CrearPostView

app_name = 'apps.posts'

urlpatterns = [
    path('', PostListViews.as_view(), name='post'),
    path("posts/<int:id>/", PostDetailViews.as_view(), name="post_individual"),
    path("posts/<int:id>/", EventoViews.as_view(), name='Evento'),
    path("posts/", CrearPostView.as_view(), name="crear_post"),
    ]