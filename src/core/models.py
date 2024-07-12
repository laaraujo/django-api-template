from django.db import models


class BaseModel(models.Model):
    """
    Model implementing audit-related fields
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        abstract = True
