from time import sleep

from os import environ

import requests

from rest_framework.response import Response
from rest_framework import status


def validate_accounts(data):
    """
    La función envía una petición de validación al microservicio core y
    si la respuesta es 200, entonces se permite cualquier acción con las cuentas,
    de otro modo se denega, como la asignación de cuentas en la creación de metas por ejemplo.
    """
    core_url = environ.get('CORE_SERVICE_URL')
    validation_path = 'validate-user-accounts/'
    accounts = []
    if 'from_account' in data and data['from_account'] is not None:
        accounts.append(data['from_account'])
    if 'to_account' in data and data['to_account'] is not None:
        accounts.append(data['to_account'])
    data = {'user': data['user'], 'accounts': accounts}
    if len(accounts) > 0:
        try:
            r = requests.post(core_url+validation_path, json=data, timeout=0.5)
            if r.status_code == 200:
                return True
            else:
                return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.RequestException:
            return Response('Service unavailable', status=status.HTTP_503_SERVICE_UNAVAILABLE)
    else:
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
