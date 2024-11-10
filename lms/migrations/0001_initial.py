# Generated by Django 4.2.2 on 2024-11-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название курса')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание курса')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='media/course/', verbose_name='Превью курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название урока')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание урока')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='media/lesson/', verbose_name='Превью урока')),
                ('link_to_video', models.URLField(max_length=100, verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
