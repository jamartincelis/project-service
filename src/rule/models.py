from uuid import uuid4

from django.db import models
from django.db.models.fields import UUIDField

from project.models import Project


class Rule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.UUIDField(db_index=True, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='rules')
    status = models.UUIDField(db_index=True, default='65729137-0844-4b28-85b5-2e81b73a948a')
    rule_type = models.UUIDField(db_index=True, null=False)
    amount = models.DecimalField(decimal_places=2, max_digits=14)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    transaciton_category = models.UUIDField(db_index=True, null=True)

    # indica qué día del mes se ejecuta la regla % de sueldo  
    fix_salary_execution_day = models.PositiveSmallIntegerField(default=0)
    # indica la frecuencia de ejecucion de las reglas monto fijo y gastar menos 
    FREQUENCY_CONDITIONS_CHOICES = [
        ('d', 'Diario'),
        ('s', 'Semanal'),
        ('q', 'Quincenal'),
        ('m', 'Mensual'),
    ]
    execution_frequency = models.CharField(default=None, null=True, max_length=1, choices=FREQUENCY_CONDITIONS_CHOICES)
    # pasion futbolera
    sport_team = models.UUIDField(null=True) 
    SPORT_CONDITIONS_CHOICES = [
        ('J', 'Juega'),
        ('G', 'Gana'),
        ('A', 'Anota'),
    ]
    sport_conditions = models.CharField(default=None, null=True, max_length=1, choices=SPORT_CONDITIONS_CHOICES)
    # desafío invierno
    weather_city = models.UUIDField(null=True) 
    temperature = models.PositiveSmallIntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'rules'