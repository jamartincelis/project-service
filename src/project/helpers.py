from time import sleep

from os import environ

import requests

from rest_framework.response import Response
from rest_framework import status

from project import serializers
from project.models import Project

from rule.models import Rule


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
    payload = {
        'user': str(data['user']), 
        'accounts': accounts
    }
    print(accounts)
    if len(accounts) > 0:
        request = requests.post('{}{}'.format(core_url, validation_path), json=payload, timeout=2)
        print(request)
        if request.status_code == 200:
            return True
        return False


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


def get_catalog(catalog_name):
    """
    Realiza una consulta al microservicio de catálogos y obtiene la información
    necesaria de un catálogo. Sirve para inicializar widgets que requieran de catálogos
    """
    catalog_url = environ.get('CATALOG_SERVICE_URL')
    try:
        print('CATALOG DATA LOADED')
        return requests.get(catalog_url+'?catalog={}'.format(catalog_name)).json()
    except requests.exceptions.RequestException:
        return {}