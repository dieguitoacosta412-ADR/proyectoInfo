from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_apellido', 'email', 'asunto', 'fecha')
    list_filter = ('fecha', 'asunto')
    search_fields = ('nombre_apellido', 'email', 'asunto')
    ordering = ('-fecha',)
    list_per_page = 20