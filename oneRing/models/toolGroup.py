from django.db import models
from django.contrib.auth.models import User
import uuid

class toolGroup(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)

    name = models.CharField(max_length=30)

    authUsers = models.ManyToManyField(User)

    def __str__(self):
        return self.name