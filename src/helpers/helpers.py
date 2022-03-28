from os import environ

import requests


def validate_accounts(data):
    """
    La función envía una petición de validación al microservicio core y
    si la respuesta es 200, entonces se permite cualquier acción con las cuentas,
    de otro modo se denega, como la asignación de cuentas en la creación de metas 
    por ejemplo.
    Si se recibe al menos una de las cuentas para crear la meta, es necesario validar
    que le pertenezcan al usuario antes de crear una meta.
    Si la petición no contiene cuentas ni de origen ni de destino, se crea la meta
    y la validación se hará al ejecutar la edición de la meta en la asignación de 
    cuentas.
    """
    core_url = environ.get('CORE_SERVICE_URL')
    validation_path = 'users/validate-user-accounts/'
    accounts = []
    if 'from_account' in data and data['from_account'] is not None:
        accounts.append(data['from_account'])
    if 'to_account' in data and data['to_account'] is not None:
        accounts.append(data['to_account'])
    if len(accounts) > 0:
        payload = {
            'user': str(data['user']), 
            'accounts': accounts
        }
        request = requests.post('{}{}'.format(core_url, validation_path), json=payload, timeout=10)
        if request.status_code == 200:
            return True
        else:
            return False
    return True


def catalog_to_dict(catalog_name):
    """
    Consulta un catálogo y lo convierte a diccionario para simular un sistema de cache propio del
    proyecto y evitar consultas http masivas
    """
    try:
        catalog_url = environ.get('CATALOG_SERVICE_URL')
        r = requests.get(catalog_url+'?catalog={}'.format(catalog_name), timeout=1)
        if r.status_code == 200:
            r = r.json()
            data = {}
            for item in r[catalog_name]:
                data[item['id']] = item
            print('Catalog {} Loaded'.format(catalog_name).upper())
            return data
        raise Exception('Failed to load catalog {}'.format(catalog_name).upper())
    except requests.exceptions.RequestException:
        raise Exception('Failed to load catalog {}'.format(catalog_name).upper())


def get_catalog(catalog_name):
    """
    Realiza una consulta al microservicio de catálogos y obtiene la información
    necesaria de un catálogo. Sirve para inicializar widgets que requieran de catálogos
    """
    catalog_url = environ.get('CATALOG_SERVICE_URL')
    try:
        r = requests.get(catalog_url+'?catalog={}'.format(catalog_name), timeout=1)
        if r.status_code == 200:
            print('Catalog {} Loaded'.format(catalog_name).upper())
            return r.json()
        raise Exception('Failed to load catalog {}'.format(catalog_name).upper())
    except requests.exceptions.RequestException:
        raise Exception('Failed to load catalog {}'.format(catalog_name).upper())


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
            "amount": float(rule.amount),
            "title": "Regla {} creada.".format(rule_type['name']),
            "message": "Regla {} creada.".format(rule_type['name']),
            "rule_name": rule_type['name'],
            "activity_type": "E"
        }
        requests.post('{}{}'.format(service_url,path), json=payload, timeout=3)
