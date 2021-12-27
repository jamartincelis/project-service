from os import environ

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from project.models import Project
from project.serializers import ProjectFrontSerializer, ProjectModelSerializer
from project.helpers import validate_accounts, get_catalog


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
        request.data['user'] = user
        # Si se recibe al menos una de las cuentas para crear la meta, es necesario validar
        # que le pertenezcan al usuario antes de crear una meta
        validation = validate_accounts(request.data)
        if validation is True:
            obj = Project.objects.create(**ProjectModelSerializer(request.data).data)
            return Response(ProjectFrontSerializer(obj).data, status=status.HTTP_201_CREATED)
        # Si la petición no contiene cuentas ni de origen ni de destino, se crea la meta
        # y la validación se hará al ejecutar la edición de la meta en la asignación de cuentas
        elif validation is False:
            project = Project.objects.create(**ProjectModelSerializer(request.data).data)
            return Response(ProjectFrontSerializer(project).data, status=status.HTTP_201_CREATED)
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
