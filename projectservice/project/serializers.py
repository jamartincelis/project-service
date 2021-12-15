from project.models import Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una meta.
    """
    class Meta:
        model = Project
        fields = '__all__'