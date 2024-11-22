from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса', **NULLABLE)
    preview = models.ImageField(upload_to='media/course/', verbose_name='Превью курса', **NULLABLE)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Владелец курса', **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока', **NULLABLE)
    preview = models.ImageField(upload_to='media/lesson/', verbose_name='Превью урока', **NULLABLE)
    link_to_video = models.URLField(max_length=100, verbose_name='Ссылка на видео')
    lesson_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Связь урока с курсом',
                                      related_name='lesson_course_set', **NULLABLE)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Владелец урока', **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
