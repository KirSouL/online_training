# Generated by Django 4.2.2 on 2024-11-10 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.course', verbose_name='Связь урока с курсом'),
        ),
    ]