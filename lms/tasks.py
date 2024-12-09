from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from dateutil.relativedelta import relativedelta

from config.settings import EMAIL_HOST_USER
from lms.models import Subscription
from users.models import User


@shared_task
def send_course_update(pk):

    subscription_course = Subscription.objects.filter(user_course=pk)
    # print(f"Найдено {len(subscription_course)} подписок на курс {pk}")
    for subscription in subscription_course:
        send_mail(
            subject=f"Обновление материалов курса {subscription.user_course.title}",
            message=f"Содержимое материалов курса: {subscription.user_course.title} обновлено",
            from_email=EMAIL_HOST_USER,
            recipient_list=[subscription.user_subscription.email],
            fail_silently=False
            )


@shared_task
def check_last_login():
    today = timezone.now()
    month_ago = today - relativedelta(months=1)
    users = User.objects.filter(last_login__lte=month_ago, is_active=True)
    users.update(is_active=False)