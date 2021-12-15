from project.models import Project
from project.serializers import ProjectSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

                                             
class HealthCheckApiView(APIView):

    def get(self, request, user):
        return Response('OK', status=status.HTTP_200_OK)

class ProjectList(ListCreateAPIView):
    """
    Devuelve la listar o crear metas.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, user):
        projects = self.get_queryset().filter(user=user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class ProjectDetail(RetrieveUpdateAPIView):
    """
    Permite retornar, actualizar o borrar un Presupuesto.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
