# Generated by Django 4.0 on 2021-12-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_project_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.UUIDField(db_index=True, default='f2a34b3c-5eea-4bfd-a18e-06d675826486'),
        ),
    ]
