from django.db import models
from django.utils import timezone


# Categorias
class Categoria(models.Model):
    nombre=models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo=models.CharField(max_length=50, null=False)
    subtitulo=models.CharField(max_length=100, null=True, blank=True)
    fecha=models.DateTimeField(auto_now_add=True)
    texto=models.TextField(null=False)
    activo=models.BooleanField(default=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='sin categoria')
    imagen=models.ImageField(null=True, blank=True, upload_to='media', default='static/post_defauld.png')
    publicado=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parents =False):
        self.imagen.delete(self.imagen.name)
        super().delete()
        

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=100)
    categoria = models.CharField(
        max_length=50,
        choices=[
            ("Naturaleza", "Naturaleza"),
            ("Cultura", "Cultura"),
            ("Gastronomía", "Gastronomía"),
        ]
    )


    def _str_(self):
        return self.nombre


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField(null=True, blank=True)
    lugar = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="eventos/", blank=True, null=True)

    class Meta:
        ordering = ('-fecha',)

    def _str_(self):
        return f"{self.titulo} - {self.fecha}-{self.hora}"


class Recomendacion(models.Model):
    titulo = models.CharField(max_length=100)
    tips_viaje = models.TextField(blank=True, null=True)
    hospedaje = models.TextField(blank=True, null=True)
    transporte = models.TextField(blank=True, null=True)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name="recomendaciones")

    def _str_(self):
        return self.titulo


class Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    archivo = models.ImageField(upload_to="galeria/")
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name="imagenes", blank=True, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="imagenes", blank=True, null=True)

    def _str_(self):
        return self.titulo