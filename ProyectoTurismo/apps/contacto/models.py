from django.db import models
from django.utils import timezone

class Contacto(models.Model):
    nombre_apellido = models.CharField(max_length=120)
    email = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # Mostrar nombre y asunto para identificar mejor cada registro
        return f"{self.nombre_apellido} - {self.asunto}"

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['-fecha']  # los más recientes primero
        return self.nombre_apellido