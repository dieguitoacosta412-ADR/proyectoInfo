from django.contrib import admin
from .models import Categotia, Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','titulo','subtitulo','fecha','texto',
                  'activo','categoria','imagen','publicado')
    



admin.site.register(Categotia)