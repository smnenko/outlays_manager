from django.conf import settings
from django.core.mail import send_mass_mail
from django.utils import timezone

from outlays_manager import celery_app
from account.models import Account
from account.utils import AccountStatisticsUtil


@celery_app.task()
def send_user_statistics_email():
    end_date = timezone.now()
    start_date = end_date - timezone.timedelta(days=1)
    subject = 'Outlays Manager Reminder - Your yesterday statistic is ready'
    send_mass_mail(
        [(
            subject,
            AccountStatisticsUtil.generate(i, start_date, end_date),
            settings.EMAIL_HOST_USER,
            [i.user.email]
        ) for i in Account.objects.all()],
        fail_silently=False
    )
