from django.db import models
from django.utils import timezone

class Contacto(models.Model):
    nombre_apellido = models.CharField("Nombre y Apellido", max_length=120)
    email = models.EmailField("Correo electrónico")
    asunto = models.CharField("Asunto", max_length=50)
    mensaje = models.TextField("Mensaje")
    fecha = models.DateTimeField("Fecha de contacto", default=timezone.now)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.nombre_apellido} - {self.asunto}"