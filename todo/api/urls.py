from django.urls import path
from todo.api import views as todo_views

urlpatterns = [
    path('todos/', todo_views.TodosApiView.as_view()),
    path('todos/<int:pk>/', todo_views.TodoDetailApiView.as_view())
]
