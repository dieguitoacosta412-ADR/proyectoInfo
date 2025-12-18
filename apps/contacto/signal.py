from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contacto

@receiver(post_save, sender=Contacto)
def notificar_contacto(sender, instance, created, **kwargs):
    if created:
        print(f"Nuevo contacto: {instance}")