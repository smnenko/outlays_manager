from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel


class Account(BaseModel, models.Model):
    user = models.OneToOneField(get_user_model(), related_name='account', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f'{str(self.user).capitalize()} account'
