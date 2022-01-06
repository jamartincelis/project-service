from rest_framework import serializers

from project.helpers import catalog_to_dict

from rule.models import Rule



class RuleFrontSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una regla.
    """

    rule_type = serializers.SerializerMethodField()
    sport_team = serializers.SerializerMethodField()
    rule_types = catalog_to_dict('rule_types')
    sport_teams = catalog_to_dict('sports_teams')

    class Meta:
        model = Rule
        fields = '__all__'

    def get_rule_type(self, obj):
        try:
            r = self.rule_types[str(obj['rule_type'])]
        except TypeError:
            r = self.rule_types[(str(obj.rule_type))]
        return r

    def get_sport_team(self, obj):
        team = obj['sport_team'] if isinstance(obj, dict) else str(obj.sport_team)
        try:
            return self.sport_teams[team]
        except KeyError:
            return None


class RuleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rule
        fields = '__all__'
