# Generated by Django 4.0 on 2021-12-28 17:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.UUIDField(db_index=True)),
                ('project', models.UUIDField(db_index=True)),
                ('status', models.UUIDField(db_index=True, default='65729137-0844-4b28-85b5-2e81b73a948a')),
                ('rule_type', models.UUIDField(db_index=True)),
                ('rule_category', models.UUIDField(db_index=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=14)),
                ('frequency', models.PositiveSmallIntegerField(default=0)),
                ('day', models.PositiveSmallIntegerField(default=0)),
                ('onboarding', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'rules',
                'managed': True,
            },
        ),
    ]