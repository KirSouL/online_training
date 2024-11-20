from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Дженерик создания пользователя"""
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """Дженерик получения всех пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Дженерик получения одного пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Дженерик обновления пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Дженерик удаления пользователя"""
    queryset = User.objects.all()


class PaymentCreateAPIView(generics.CreateAPIView):
    """Дженерик создания платежа"""
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    """Дженерик получения всех платежей"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['payment_date']
    filterset_fields = ('user', 'payment_course', 'payment_lesson', 'payment_method',)


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    """Дженерик получения одного платежа"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDestroyAPIView(generics.DestroyAPIView):
    """Дженерик удаления платежа"""
    queryset = Payment.objects.all()
