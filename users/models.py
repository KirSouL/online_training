from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    token = models.CharField(max_length=150, verbose_name='token', **NULLABLE)

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=150, verbose_name='Отчество', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)

    avatar = models.ImageField(upload_to='media/users/', verbose_name='Аватар профиля', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=200, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}, {self.first_name}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payment(models.Model):
    class ChoicePaymentMethod(models.TextChoices):
        TRANSFER = 'T', 'Оплата переводом'
        CASH = 'C', 'Оплата наличностью'

    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    payment_date = models.DateField(auto_now_add=True, verbose_name='Дата оплаты', **NULLABLE)
    payment_course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='Оплата курса', **NULLABLE)
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT, verbose_name='Оплата урока', **NULLABLE)
    summ_payment = models.PositiveIntegerField(default=0, verbose_name='Сумма к оплате', **NULLABLE)
    payment_method = models.CharField(max_length=1, verbose_name='Метод оплаты', choices=ChoicePaymentMethod.choices,
                                      default=ChoicePaymentMethod.TRANSFER)

    session_id = models.CharField(max_length=255, verbose_name='id сессии', **NULLABLE)
    link_to_payment = models.URLField(max_length=400, verbose_name='Ссылка на страничку оплаты переводом', **NULLABLE)

    def __str__(self):
        return f"{self.user}, {self.payment_method}"

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
