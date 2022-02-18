from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rule.serializers import RuleSerializer
from rule.models import Rule

class RuleList(ListCreateAPIView):
    """
    Permite crear una regla y así como también retornar la lista de reglas
    """
    serializer_class = RuleSerializer

    def get_queryset(self):

        STATUS_ACTIVE = '65729137-0844-4b28-85b5-2e81b73a948a'
        MANUAL_SAVING = 'd53ff871-c9e1-407a-b292-872d38f0bddd'

        queryset = Rule.objects.filter(
            user=self.kwargs['user'], project=self.kwargs['project'],
            status=STATUS_ACTIVE).exclude(rule_type=MANUAL_SAVING)

        return queryset

class RuleDetail(RetrieveUpdateAPIView):
    """
    Permite retornar y actualizar una regla.
    """
    serializer_class = RuleSerializer

    def get_queryset(self):
        return Rule.objects.filter(user=self.kwargs['user'], project=self.kwargs['project'], pk=self.kwargs['pk'])
