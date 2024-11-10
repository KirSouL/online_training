from django.urls import path

from users.apps import UsersConfig
from users.views import UserList

app_name = UsersConfig.name

urlpatterns = [
    path('users/', UserList.as_view(), name='users-list'),
]
