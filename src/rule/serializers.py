from rest_framework import serializers

from project.helpers import catalog_to_dict

from rule.models import Rule


class RuleSerializer(serializers.ModelSerializer):
    # catalogos de tipos de regla
    rule_type_catalogs = catalog_to_dict('rule_types')

    class Meta:
        model = Rule
        fields = '__all__'

    def get_rule_type_object(self, pk):
        try:
            r = self.rule_type_catalogs[str(pk)]
        except TypeError:
            r = self.rule_type_catalogs[(str(pk))]
        return r

    def to_representation(self, instance):
        data = super(RuleSerializer, self).to_representation(instance)
        data['rule_type'] = self.get_rule_type_object(data['rule_type'])
        data.update(data)
        return data

    def to_internal_value(self, data):
        data['user'] = self.context.get("request").parser_context["kwargs"]["user"]
        data['project'] = self.context.get("request").parser_context["kwargs"]["project"]
        return super().to_internal_value(data)
