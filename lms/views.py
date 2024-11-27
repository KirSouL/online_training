from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from lms.models import Course, Lesson, Subscription
from lms.paginators import ListPaginator
from lms.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from users.permissions import IsOwner, IsModerator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = ListPaginator

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
            self.permission_classes = [IsOwner | ~IsModerator]
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
    pagination_class = ListPaginator


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


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('user_course')
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = Subscription.objects.filter(user_subscription=user, user_course=course_item)
        if subs_item.exists():
            Subscription.objects.get(user_subscription=user, user_course=course_item).delete()
            message = 'подписка удалена'
        else:
            Subscription.objects.create(user_subscription=user, user_course=course_item)
            message = 'подписка добавлена'

        return Response({"message": message})
