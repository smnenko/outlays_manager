from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel


class Category(BaseModel, models.Model):
    user = models.ForeignKey(get_user_model(), related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{str(self.user).capitalize()} - {self.name}'

    class Meta:
        verbose_name_plural = 'categories'
