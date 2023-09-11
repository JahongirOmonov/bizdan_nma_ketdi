from django.db import models
from datetime import datetime

# Create your models here.


class todoModel(models.Model):
    task_name = models.CharField(max_length=200, default='')
    create_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)
    description = models.TextField(default='write here')

    class Meta:
        db_table = 'info'

    def __str__(self) -> str:
        return self.task_name
