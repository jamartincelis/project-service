# Generated by Django 4.0 on 2022-03-03 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0008_remove_rule_day_remove_rule_onboarding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='execution_frequency',
            field=models.CharField(choices=[('D', 'Diario'), ('S', 'Semanal'), ('Q', 'Quincenal'), ('M', 'Mensual')], default=None, max_length=1, null=True),
        ),
    ]
