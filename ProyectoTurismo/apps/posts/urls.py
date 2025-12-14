from django.urls import path
from .views import PostListViews, PostDetailViews, EventoViews

app_name= 'apps.posts'

urlpatterns= [ 
    path('posts/', PostListViews.as_view(), name= 'posts'),
    path("posts/<int:id>/", PostDetailViews.as_view(), name="post_individual"),
    path("posts/<int:id>/", EventoViews.as_view(), name= 'Evento'),
   
]