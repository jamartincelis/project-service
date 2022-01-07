# Generated by Django 4.0 on 2022-01-02 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_project_from_account_alter_project_to_account'),
        ('rule', '0002_alter_rule_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='project.project'),
        ),
    ]