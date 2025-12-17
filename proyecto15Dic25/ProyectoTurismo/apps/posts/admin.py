from django.contrib import admin
from .models import Categoria, Post, Evento

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','titulo','subtitulo','fecha','texto',
                  'activo','categoria','imagen','publicado')
    



admin.site.register(Categoria)
admin.site.register(Evento)