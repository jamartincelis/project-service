from uuid import uuid4
from django.db import models
from django.db.models.fields import UUIDField

class Project(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    user = models.UUIDField(db_index=True, null=False)
    status = models.UUIDField(db_index=True, 
        default='f2a34b3c-5eea-4bfd-a18e-06d675826486')
    category = models.UUIDField(db_index=True, null=False)
    name = models.CharField(max_length=60, )
    goal_date = models.DateField()
    deleted_at = models.DateTimeField(null=True, default=None)
    total = models.DecimalField(decimal_places=2, max_digits=14, default=0)
    progress = models.DecimalField(decimal_places=2, max_digits=14, default=0)
    processing = models.DecimalField(decimal_places=2, max_digits=14, default=0)
    pending = models.DecimalField(decimal_places=2, max_digits=14, default=0)
    from_account = models.CharField(max_length=60, null=True)
    to_account = models.CharField(max_length=60, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'projects'
