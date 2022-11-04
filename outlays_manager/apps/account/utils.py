from django.db.models import Count, Sum
from django.utils import timezone

from account.models import Account


class AccountStatisticsUtil:

    @classmethod
    def generate(cls, account: Account, start_date: timezone.timezone, end_date: timezone.timezone):
        past_transactions = account.transactions.filter(
            created_at__gt=start_date, created_at__lt=end_date
        )
        categories_totals = (
            past_transactions
            .values('total', 'category')
            .aggregate(sum=Sum('total'), count=Count('category'))
        )
        return (
            f'Current balance: {account.balance}\n\n'
            f'Transactions performed:\n'
            f'    - Total: {account.transactions.count()}\n'
            f'    - Yesterday: {past_transactions.count()}\n\n'
            f"Balance has been changed from {categories_totals['count']} categories by {categories_totals['sum']}\n"
        )



