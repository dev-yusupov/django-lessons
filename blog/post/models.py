from django.db import models

from uuid import uuid4

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title