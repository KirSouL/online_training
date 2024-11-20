from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_course_set", many=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'preview', 'count_lesson', 'lessons')

    def get_count_lesson(self, instanse):
        return instanse.lesson_course_set.count()
