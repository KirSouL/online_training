from rest_framework import viewsets, generics

from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    """Дженерик создания урока"""
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """Дженерик получения всех уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Дженерик получения одного урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Дженерик обновления урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Дженерик удаления урока"""
    queryset = Lesson.objects.all()
