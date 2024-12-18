from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from lms.paginators import ListPaginator
from users.models import User, Payment
from users.permissions import IsOwner
from users.serializers import UserSerializer, PaymentSerializer
from users.services import create_stripe_product, create_stripe_payment, create_stripe_url


class UserCreateAPIView(generics.CreateAPIView):
    """Дженерик создания пользователя"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """Дженерик получения всех пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    pagination_class = ListPaginator


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Дженерик получения одного пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Дженерик обновления пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDestroyAPIView(generics.DestroyAPIView):
    """Дженерик удаления пользователя"""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentCreateAPIView(generics.CreateAPIView):
    """Дженерик создания платежа"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        payment_user = serializer.save(user=self.request.user)
        create_product = create_stripe_product(payment_user)
        create_payment = create_stripe_payment(payment_user.summ_payment, create_product)
        session_id, link_to_payment = create_stripe_url(create_payment)
        payment_user.session_id = session_id
        payment_user.link_to_payment = link_to_payment
        payment_user.save()


class PaymentListAPIView(generics.ListAPIView):
    """Дженерик получения всех платежей"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]
    pagination_class = ListPaginator
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
    permission_classes = [IsAuthenticated, IsOwner]
