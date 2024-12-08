from datetime import timedelta
from django.utils import timezone
from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from lms.models import Course
from lms.serializers import CourseSerializer
from users.models import User


@shared_task
def send_course_update(pk):
    course = Course.objects.get(id=pk)
    serializer = CourseSerializer(course)
    email = serializer.get_subscription_course(course)
    send_mail = (
        f'Обновление курса {course.title}',
        'Для Вас доступны обновления курса',
        EMAIL_HOST_USER,
        [email],
    )


@shared_task
def check_last_login():
    users = User.objects.filter(last_login__isnull=False)
    today = timezone.now()
    for user in users:
        if today - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
            print('Пользователь заблокирован')
        else:
            print('Действующий пользователь')
