from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from project.models import Project

from rule.serializers import RuleModelSerializer, RuleFrontSerializer
from rule.models import Rule


class RuleList(ListCreateAPIView):
    """
    Permite crear una regla y así como también retornar la lista de reglas
    """
    queryset = Rule.objects.all()
    serializer_class = RuleFrontSerializer

    def get(self, request, user, project):
        """
        Permite retornar las reglas asociadas a la meta de un usuario.
        """
        STATUS_ACTIVE = '65729137-0844-4b28-85b5-2e81b73a948a'
        MANUAL_SAVING = 'd53ff871-c9e1-407a-b292-872d38f0bddd'
        rules = self.get_queryset().filter(
            user=user, project=project, status=STATUS_ACTIVE
        ).exclude(rule_type=MANUAL_SAVING) # activas y que no sean tipo ahorro manual
        data = RuleFrontSerializer(rules, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


    def post(self, request, user, project):
        """
        Permite crear una regla
        """
        try:
            project = Project.objects.get(user=user, pk=project)
        except Project.DoesNotExist:
            return Response('Not found.', status.HTTP_404_NOT_FOUND)
        data = request.data
        data['user'] = user
        data['project'] = project.id
        model_serializer = RuleModelSerializer(data=data)
        if model_serializer.is_valid():
            obj = model_serializer.save()
            return Response(RuleFrontSerializer(obj).data, status=status.HTTP_201_CREATED)
        return Response(model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RuleDetail(RetrieveUpdateAPIView):
    """
    Permite retornar y actualizar una regla.
    """
    serializer_class = RuleFrontSerializer
    queryset = Rule.objects.all()

    def update(self, request, *args, **kwargs):
        try:
            Project.objects.get(user=kwargs['user'], pk=kwargs['project'])
        except Project.DoesNotExist:
            return Response("Not found.", status.HTTP_404_NOT_FOUND)

        try:
            rule = Rule.objects.get(user=kwargs['user'], pk=kwargs['pk'])
        except Rule.DoesNotExist:
            return Response("Not found.", status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            model_serializer = RuleModelSerializer(data=request.data)
            if not model_serializer.is_valid():
                return Response(model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        rule.__dict__.update(request.data)
        rule.save()
        return Response(self.serializer_class(rule).data, status=status.HTTP_200_OK)
