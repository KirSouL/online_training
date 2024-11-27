from rest_framework import serializers

from lms.models import Course, Lesson, Subscription
from lms.validators import YouTubeValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YouTubeValidator(field='link_to_video')]


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_course_set", many=True, read_only=True)
    subscription_course = serializers.SerializerMethodField()

    def get_count_lesson(self, instance):
        return instance.lesson_course_set.count()

    def get_subscription_course(self, instance):
        request = self.context.get('request')
        user = None

        if request:
            user = request.user

        return instance.subscription_set.filter(user_subscription=user).exists()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'preview', 'count_lesson', 'lessons', 'owner', 'subscription_course',)


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
