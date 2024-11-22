from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsOwner, IsModerator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsOwner, ~IsModerator]
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = [IsOwner | IsModerator]
        elif self.permission_classes == 'list':
            self.permission_classes = [AllowAny]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwner, ~IsModerator]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    """Дженерик создания урока"""
    serializer_class = LessonSerializer
    permission_classes = [~IsModerator, IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """Дженерик получения всех уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Дженерик получения одного урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsModerator,)


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Дженерик обновления урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsModerator,)


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Дженерик удаления урока"""
    queryset = Lesson.objects.all()
    permission_classes = (IsOwner | ~IsModerator,)
