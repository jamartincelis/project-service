from time import sleep

from os import environ

import requests

from rest_framework.response import Response
from rest_framework import status 
from project import serializers
from rule.models import Rule
from project.models import Project

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
    data = {'user': data['user'], 'accounts': accounts}
    if len(accounts) > 0:
        try:
            r = requests.post(core_url+validation_path, json=data, timeout=0.5)
            if r.status_code == 200:
                return True
            else:
                return Response(r.text, status=status.HTTP_400_BAD_REQUEST)
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


def invalid_rules(data_rules_list=None):
    """
    Valida un conjuntos de reglas
    """
    if len(data_rules_list) > 0:
        model_serializer = serializers.AuxiliaryRuleModelSerializer(data=data_rules_list, many=True)
        if not model_serializer.is_valid():
            return model_serializer.errors
    return False

def create_project_with_rules(project_data=None, data_rules_list=None):
    """
    Permite crear una meta con un conjuntos de reglas.
    """
    project = Project.objects.create(**serializers.ProjectModelSerializer(project_data).data)
    rules = []
    for rule in data_rules_list:
        rule['user'] = project_data['user']
        rule['project'] = project
        rules.append(rule)
    
    created_rules = Rule.objects.bulk_create([Rule(**rule) for rule in rules])
    created_project_data = serializers.ProjectFrontSerializer(project).data
    created_project_data['rules_list'] = serializers.RuleFrontSerializer(created_rules, many=True).data

    return created_project_data

def create_project(data=None):
    """
    Función principal que permite la creación de metas.
    """
    # se valida la meta
    model_serializer = serializers.ProjectModelSerializer(data=data)
    if not model_serializer.is_valid():
        return Response(model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # se validan las reglas
    data_rules_list = data.get('rules_list')
    invalid = invalid_rules(data_rules_list)
    if invalid:
        return Response(invalid, status=status.HTTP_400_BAD_REQUEST)

    # se validan las cuentas
    validation = validate_accounts(data)
    if validation in (True,False):
        created_project_data = create_project_with_rules(data, data_rules_list)
        return Response(created_project_data, status=status.HTTP_201_CREATED)
    # Se retorna cualquier error que no permita la creación de la meta (errores de red)
    return validation

def update_project(request=None, kwargs=None):
    """
    Permite actualizar una meta.
    """
    try:
        project = Project.objects.get(user=kwargs['user'], pk=kwargs['pk'])
    except Project.DoesNotExist:
        return Response("Not found.", status.HTTP_404_NOT_FOUND)

    data = request.data
    data['user'] = kwargs['user']
    have_accounts = []
    if 'from_account' in data and data['from_account'] is not None:
        have_accounts.append(True)
    if 'to_account' in data and data['to_account'] is not None:
        have_accounts.append(True)
    
    if have_accounts and all(have_accounts):
        are_valids = validate_accounts(data)
        if are_valids is not True:
            return are_valids
            
    if request.method == 'PUT':
        model_serializer = serializers.ProjectModelSerializer(data=request.data)
        if not model_serializer.is_valid():
            return Response(model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    project.__dict__.update(request.data)
    project.save()
    return Response(serializers.ProjectFrontSerializer(project).data, status=status.HTTP_200_OK)
