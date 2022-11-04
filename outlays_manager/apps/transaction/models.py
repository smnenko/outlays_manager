from django.db import models

from account.models import Account
from core.models import BaseModel
from category.models import Category


class TransactionsQuerySet(models.QuerySet):

    def delete(self):
        total = sum(i.total for i in self)
        account = Account.objects.get(pk=self.first().account.id)
        account.balance -= total
        account.save(update_fields=('balance',))
        return super().delete()


class TransactionsManager(models.Manager):

    def get_queryset(self):
        return TransactionsQuerySet(self.model, using=self._db)


class Transaction(BaseModel, models.Model):
    account = models.ForeignKey(Account, related_name='transactions', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='transactions', on_delete=models.CASCADE)

    total = models.DecimalField(max_digits=10, decimal_places=2)
    organization = models.CharField(max_length=128)
    description = models.TextField(null=True)

    objects = TransactionsManager()

    def __str__(self):
        return f"{str(self.account.user)} {self.total}"

    def save(self, *args, **kwargs):
        old_transaction = Transaction.objects.filter(pk=self.pk)
        if old_transaction.exists():
            self.account.balance -= old_transaction.first().total
        self.account.balance += self.total
        self.account.save(update_fields=('balance',))
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.account.balance -= self.total
        self.account.save(update_fields=('balance',))
        return super().delete(*args, **kwargs)
