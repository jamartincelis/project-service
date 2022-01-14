from os import environ

import requests as re

from rest_framework import serializers

from project.models import Project
from project.helpers import catalog_to_dict

from rule.serializers import RuleFrontSerializer
from rule.models import Rule


class ProjectFrontSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una meta.
    """

    category = serializers.SerializerMethodField()
    project_type = catalog_to_dict('project_type')
    rules_list = RuleFrontSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

    def get_category(self, obj):
        try:
            r = self.project_type[str(obj['category'])]
        except TypeError:
            r = self.project_type[(str(obj.category))]
        return r


class ProjectModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class AuxiliaryRuleModelSerializer(serializers.ModelSerializer):
    """
    Serializador auxiliar para el modelo de reglas
    """
    class Meta:
        model = Rule
        exclude = ('project', 'user')
