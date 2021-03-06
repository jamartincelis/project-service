from os import environ

import requests

from django.db.models.signals import post_save
from django.dispatch import receiver

from helpers.helpers import catalog_to_dict

from rule.models import Rule


# catalogos de tipos de regla
rule_type_catalogs = catalog_to_dict('rule_types')

def get_rule_type_object(pk):
    try:
        r = rule_type_catalogs[str(pk)]
    except TypeError:
        r = rule_type_catalogs[(str(pk))]
    return r


@receiver(post_save, sender=Rule)
def rule_signal(sender, instance, created, **kwargs):
    """
    Crea un registro de actividad para la nueva regla.
    """
    service_url = environ.get('ACTIVITY_SERVICE_URL')
    path = 'users/{}/projects/{}/activities/'.format(instance.user, instance.project.id)
    rule_type = get_rule_type_object(instance.rule_type)
    if created:
        message = "Regla {} creada.".format(rule_type['name'])
        icon = '/assets/xerpa/global/img/icons/add_circle.svg'
    elif not created:
        if instance.status == '94bcd197-0d33-40e4-8793-78aa42ad3220':
            message = "Regla {} pausada.".format(rule_type['name'])
            icon = '/assets/xerpa/global/img/icons/pause_circle.svg'
        else:
            message = "Regla {} actualizada.".format(rule_type['name'])
            icon = '/assets/xerpa/global/img/icons/edit_circle.svg'
    payload = {
        "user": str(instance.user),
        "project": str(instance.project),
        "rule": str(instance.id),
        "project_name": instance.project.name,
        "amount": float(instance.amount),
        "title": message,
        "message": message,
        "rule_name": rule_type['name'],
        "activity_type": "E",
        "icon": icon
    }
    requests.post('{}{}'.format(service_url,path), json=payload, timeout=3)
