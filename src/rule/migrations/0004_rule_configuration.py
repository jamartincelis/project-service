# Generated by Django 4.0 on 2022-01-03 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0003_alter_rule_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='configuration',
            field=models.JSONField(default=None, null=True),
        ),
    ]
