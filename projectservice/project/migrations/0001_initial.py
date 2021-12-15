# Generated by Django 4.0 on 2021-12-15 04:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.UUIDField(db_index=True)),
                ('status', models.UUIDField(db_index=True, default='d7d30bcd-8417-47c9-b294-a4ca5bfd3506')),
                ('category', models.UUIDField(db_index=True)),
                ('name', models.CharField(max_length=60)),
                ('goal_date', models.DateField()),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('total', models.IntegerField()),
                ('progress', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('processing', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('pending', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('from_account', models.CharField(max_length=60)),
                ('to_account', models.CharField(max_length=60)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'projects',
                'managed': True,
            },
        ),
    ]
