from os import environ

import requests


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


def create_activity(rules):
    """
    Crea registros de actividad para las reglas nuevas
    """
    service_url = environ.get('ACTIVITY_SERVICE_URL')
    for rule in rules:
        path = 'users/{}/projects/{}/activities/'.format(str(rule.user), str(rule.project.id))
        rule_type = get_rule_type_object(rule.rule_type)
        payload = {
            "user": str(rule.user),
            "project": str(rule.project),
            "rule": str(rule.id),
            "project_name": rule.project.name,
            "amount": rule.amount,
            "title": "Regla {} creada.".format(rule_type['name']),
            "message": "Regla {} creada.".format(rule_type['name']),
            "rule_name": rule_type['name'],
            "activity_type": "E"
        }
        requests.post('{}{}'.format(service_url,path), json=payload, timeout=3)
