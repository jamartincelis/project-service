# Generated by Django 4.0 on 2022-01-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0006_remove_rule_configuration_remove_rule_frequency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='transaciton_category',
            field=models.UUIDField(db_index=True, null=True),
        ),
    ]