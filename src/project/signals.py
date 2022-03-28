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
        message = "Meta {} creada.".format(instance.name)
        icon = '/assets/xerpa/global/img/icons/add_circle.svg'
    elif not created:
        if instance.status == 'b1da15e4-7011-45f3-8a99-0bde59042bc2':
            icon = '/assets/xerpa/global/img/icons/expired_circle.svg'
            message = "Meta {} eliminada.".format(instance.name)
        else:
            icon = '/assets/xerpa/global/img/icons/edit_circle.svg'
            message = "Meta {} actualizada.".format(instance.name)
    payload = {
        "user": str(instance.user),
        "project": str(instance.id),
        "project_name": instance.name,
        "amount": float(instance.total),
        "title": message,
        "message": message,
        "activity_type": "E",
        "rule": None,
        "icon": icon
    }       
    requests.post('{}{}'.format(service_url,path), json=payload, timeout=3)
