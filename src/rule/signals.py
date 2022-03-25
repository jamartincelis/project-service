from os import environ

import requests

from django.db.models.signals import post_save
from django.dispatch import receiver

from rule.models import Rule


def catalog_to_dict(catalog_name):
    """
    Consulta un catálogo y lo convierte a diccionario para simular un sistema de cache propio del
    proyecto y evitar consultas http masivas
    """
    catalog_url = environ.get('CATALOG_SERVICE_URL')
    try:
        r = requests.get(catalog_url+'?catalog={}'.format(catalog_name)).json()
        data = {}
        for item in r[catalog_name]:
            data[item['id']] = item
        print('CATALOG DATA LOADED')
        return data
    except requests.exceptions.RequestException:
        return {}


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
    path = 'users/{}/projects/{}/activities/'.format(instance.user,instance.id)
    rule_type = get_rule_type_object(instance.rule_type)
    if created:
        mensaje = "Regla {} creada.".format(rule_type['name'])
    elif not created:
        mensaje = "Regla {} actualizada.".format(rule_type['name'])
    payload = {
        "user": str(instance.user),
        "project": str(instance.project),
        "rule": str(instance.id),
        "project_name": instance.project.name,
        "amount": instance.amount,
        "title": mensaje,
        "message": mensaje,
        "rule_name": rule_type['name'],
        "activity_type": "E"
    }
    requests.post('{}{}'.format(service_url,path), json=payload, timeout=3)
