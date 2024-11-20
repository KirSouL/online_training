from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    UserRetrieveAPIView, PaymentListAPIView, PaymentRetrieveAPIView, PaymentCreateAPIView, PaymentDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('users_home/', UserListAPIView.as_view(), name='users-list'),
    path('users_home/view/<int:pk>', UserRetrieveAPIView.as_view(), name='users-view'),

    path('users_home/create/', UserCreateAPIView.as_view(), name='users-create'),

    path('users_home/update/<int:pk>', UserUpdateAPIView.as_view(), name='users-update'),
    path('users_home/delete/<int:pk>', UserDestroyAPIView.as_view(), name='users-delete'),

    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/view/<int:pk>', PaymentRetrieveAPIView.as_view(), name='payment-view'),

    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),

    path('payment/delete/<int:pk>', PaymentDestroyAPIView.as_view(), name='payment-delete'),
]
