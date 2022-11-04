from django.utils import timezone

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        if 'update_fields' in kwargs.keys():
            kwargs['update_fields'] = list(kwargs['update_fields']).append('updated_at')
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
