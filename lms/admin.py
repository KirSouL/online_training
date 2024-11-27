from django.contrib import admin

from lms.models import Course, Lesson, Subscription


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


@admin.register(Subscription)
class AdminSubscription(admin.ModelAdmin):
    list_display = ('id', 'user_subscription', 'user_course')
