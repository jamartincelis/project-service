from os import environ

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from project.models import Project
from project.serializers import ProjectSerializer
from project.helpers import get_catalog, create_project, update_project

class ProjectList(ListCreateAPIView):
    """
    Devuelve un listado de metas o crea una nueva meta.
    """
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(user=self.kwargs['user'])

    def post(self, request, user):
        """
        Permite crear una meta y sus reglas
        """
        data = request.data
        data['user'] = user

        return create_project(data)


class ProjectDetail(RetrieveUpdateAPIView):
    """
    Obtiene o actualiza una meta.
    """
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        return Project.objects.filter(user=self.kwargs['user'], pk=self.kwargs['pk'])

    def update(self, request, *args, **kwargs):
        return update_project(request,kwargs)

class NewProjectWidget(APIView):

    def get(self, request):
        return Response(get_catalog('project_type'), status=status.HTTP_200_OK)
