from django.contrib.auth.models import AbstractUser
from django.db import models

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
