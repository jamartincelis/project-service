from os import environ

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from project.models import Project
from project.serializers import ProjectSerializer
from project.helpers import get_catalog, validate_accounts


class ProjectList(ListCreateAPIView):
    """
    Devuelve un listado de metas o crea una nueva meta.
    """
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(user=self.kwargs['user'])


class ProjectDetail(RetrieveUpdateAPIView):
    """
    Obtiene o actualiza una meta.
    """

    def get(self, request, user, pk):
        try:
            project = ProjectSerializer(Project.objects.get(user=user, pk=pk)).data
            return Response(project, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response('Project not found.', status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, user, pk):
        try:
            project = Project.objects.get(user=user, pk=pk)
            for attr, value in request.data.items():
                setattr(project, attr, value)
                project.save()
            return Response(ProjectSerializer(project).data, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response('Project not found.', status=status.HTTP_200_OK)


class NewProjectWidget(APIView):

    def get(self, request):
        return Response(get_catalog('project_type'), status=status.HTTP_200_OK)
