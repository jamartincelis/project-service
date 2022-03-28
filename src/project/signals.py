from os import environ

import requests

from django.db.models.signals import post_save
from django.dispatch import receiver

from project.models import Project


@receiver(post_save, sender=Project)
def project_signal(sender, instance, created, **kwargs):
    """
    Crea un registro de actividad para la meta nueva
    """
    service_url = environ.get('ACTIVITY_SERVICE_URL')
    path = 'users/{}/projects/{}/activities/'.format(instance.user,instance.id)
    if created:
        mensaje = "Meta {} creada.".format(instance.name)
    elif not created:
        mensaje = "Meta {} actualizada.".format(instance.name)
    payload = {
        "user": str(instance.user),
        "project": str(instance.id),
        "project_name": instance.name,
        "amount": float(instance.total),
        "title": mensaje,
        "message": mensaje,
        "activity_type": "E",
        "rule": None
    }       
    requests.post('{}{}'.format(service_url,path), json=payload, timeout=3)
