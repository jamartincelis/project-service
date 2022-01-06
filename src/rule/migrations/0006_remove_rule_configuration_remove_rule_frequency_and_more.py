# Generated by Django 4.0 on 2022-01-05 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0005_remove_rule_rule_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rule',
            name='configuration',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='frequency',
        ),
        migrations.AddField(
            model_name='rule',
            name='execution_frequency',
            field=models.CharField(choices=[('d', 'Diario'), ('s', 'Semanal'), ('q', 'Quincenal'), ('m', 'Mensual')], default=None, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='rule',
            name='fix_salary_execution_day',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rule',
            name='sport_conditions',
            field=models.CharField(choices=[('J', 'Juega'), ('G', 'Gana'), ('A', 'Anota')], default=None, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='rule',
            name='sport_team',
            field=models.UUIDField(null=True),
        ),
        migrations.AddField(
            model_name='rule',
            name='temperature',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rule',
            name='weather_city',
            field=models.UUIDField(null=True),
        ),
    ]
