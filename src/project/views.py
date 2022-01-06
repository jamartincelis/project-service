from os import environ

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from project.models import Project
from project.serializers import ProjectFrontSerializer, ProjectModelSerializer, AuxiliaryRuleModelSerializer
from project.helpers import validate_accounts, get_catalog

from rule.models import Rule
from rule.serializers import RuleFrontSerializer


class ProjectList(ListCreateAPIView):
    """
    Devuelve un listado de metas o crea una nueva meta.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectFrontSerializer

    def get(self, request, user):
        projects = self.get_queryset().filter(user=user)
        serializer = ProjectFrontSerializer(projects, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user):
        """
        Permite crear una meta y sus reglas
        """
        data = request.data
        data['user'] = user
    
        # se validan las reglas
        data_rules_list = data.get('rules_list')        
        if len(data_rules_list) > 0:
            model_serializer = AuxiliaryRuleModelSerializer(data=data_rules_list, many=True)
            if not model_serializer.is_valid():
                return Response(model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Si se recibe al menos una de las cuentas para crear la meta, es necesario validar
        # que le pertenezcan al usuario antes de crear una meta
        # Si la petición no contiene cuentas ni de origen ni de destino, se crea la meta
        # y la validación se hará al ejecutar la edición de la meta en la asignación de cuentas

        validation = validate_accounts(data)
        if validation in (True,False):
            project = Project.objects.create(**ProjectModelSerializer(data).data)
            rules = []
            for rule in data_rules_list:
                rule['user'] = user
                rule['project'] = project
                rules.append(rule)
            
            created_rules = Rule.objects.bulk_create([Rule(**rule) for rule in rules])
            created_project_data = ProjectFrontSerializer(project).data
            created_project_data['rules_list'] = RuleFrontSerializer(created_rules, many=True).data

            return Response(created_project_data, status=status.HTTP_201_CREATED)
        # Se retorna cualquier error que no permita la creación de la meta (errores de red)
        return validation


class ProjectDetail(RetrieveUpdateAPIView):
    """
    Obtiene o actualiza una meta.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectFrontSerializer


class NewProjectWidget(APIView):

    def get(self, request):
        return Response(get_catalog('project_type'), status=status.HTTP_200_OK)
