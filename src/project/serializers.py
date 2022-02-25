from os import environ
import requests as re
from rest_framework import serializers
from project.models import Project
from project.helpers import catalog_to_dict
from rule.models import Rule
from .helpers import validate_accounts
from rule.serializers import RuleSerializer
from rest_framework.response import Response

class ProjectSerializer(serializers.ModelSerializer):
    
    project_type_catalogs = catalog_to_dict('project_type')
    rules = RuleSerializer(read_only=True, many=True)

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
        Permite modificar la forma en que se retornan las metas.
        """
        data = super(ProjectSerializer, self).to_representation(instance)
        data['category'] = self.get_object_category(data['category'])
        
        try:
            # rename rules to rules_list 
            data['rules_list'] = data.pop('rules')
        except KeyError:
            data['rules_list'] = self.initial_data['rules_list']
        data.update(data)

        return data

    def to_internal_value(self, data):
        data['user'] = self.context.get("request").parser_context["kwargs"]["user"]
        return super().to_internal_value(data)

    def validate(self, data):
        from_account = data.get('from_account')
        to_account = data.get('to_account')
        
        if from_account and to_account:
            # validar cuentas
            message = validate_accounts(data).strip('"')
            if message != "OK":
                raise serializers.ValidationError(message)
        return data

    def create(self, validated_data):
        # se valida que este presente en el request
        if not "rules_list" in self.initial_data:
            raise serializers.ValidationError("rules_list is required.")
        
        # si tiene reglas, se validan
        rules_list = self.initial_data['rules_list']

        if len(rules_list) > 0:
            model_serializer = AuxiliaryRuleModelSerializer(data=rules_list, many=True)
            if not model_serializer.is_valid():
                return model_serializer.errors

        project = Project.objects.create(**validated_data)

        # se crean las reglas
        rules = []
        for rule in rules_list:
            rule['user'] = validated_data['user']
            rule['project'] = project
            rules.append(rule)
    
        created_rules = Rule.objects.bulk_create([Rule(**rule) for rule in rules])
        self.initial_data['rules_list'] = RuleSerializer(created_rules, many=True).data
        
        return self.initial_data

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class AuxiliaryRuleModelSerializer(serializers.ModelSerializer):
    """
    Serializador auxiliar para el modelo de reglas
    """
    class Meta:
        model = Rule
        exclude = ('project', 'user')
