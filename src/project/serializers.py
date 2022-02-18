from os import environ
import requests as re
from rest_framework import serializers
from project.models import Project
from project.helpers import catalog_to_dict
from rule.models import Rule


class ProjectSerializer(serializers.ModelSerializer):
    
    project_type_catalogs = catalog_to_dict('project_type')

    class Meta:
        model = Project
        fields = '__all__'

    def get_object_category(self, pk):
        try:
            r = self.project_type_catalogs[str(pk)]
        except TypeError:
            r = self.project_type_catalogs[(str(pk))]
        return r

    def to_representation(self, instance):
        """
        Permite modificar la forma en que se retornan las metas
        """
        data = super(ProjectSerializer, self).to_representation(instance)
        data['category'] = self.get_object_category(data['category'])
        data.update(data)

        return data

class AuxiliaryRuleModelSerializer(serializers.ModelSerializer):
    """
    Serializador auxiliar para el modelo de reglas
    """
    class Meta:
        model = Rule
        exclude = ('project', 'user')
