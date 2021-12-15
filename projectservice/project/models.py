from uuid import uuid4
from django.db import models
from django.db.models.fields import UUIDField

class Project(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    user = models.UUIDField(db_index=True, null=False)
    status = models.UUIDField(db_index=True, 
        default='d7d30bcd-8417-47c9-b294-a4ca5bfd3506')
    category = models.UUIDField(db_index=True, null=False)
    name = models.CharField(max_length=60, )
    goal_date = models.DateField()
    deleted_at = models.DateTimeField(null=True, default=None)
    total = models.IntegerField()
    progress = models.DecimalField(decimal_places=2, max_digits=14, default=0)
    processing = models.DecimalField(decimal_places=2, max_digits=14, default=0)
    pending = models.DecimalField(decimal_places=2, max_digits=14, default=0)
    from_account = models.CharField(max_length=60)
    to_account = models.CharField(max_length=60)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'projects'