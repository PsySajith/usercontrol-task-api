from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    ListAllTodosView, ListUserTodoView, TodoDetailView, CompletedTodoListView
)

urlpatterns = [
    path('task/', ListAllTodosView.as_view(), name='list'),
    path('tasks/', ListUserTodoView.as_view(), name='restrict'),
    path('tasks/<int:pk>/', TodoDetailView.as_view(), name='detail'),
    path('task/filter/', CompletedTodoListView.as_view(), name="complete"),

    # token url
    path('token/', obtain_auth_token, name='api_token_auth'),
]
