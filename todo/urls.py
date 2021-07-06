from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.HomeView.as_view(), name='todo-home'),
    path('add_todo/', views.AddTodoView.as_view(), name='todo-add'),
    path('delete_todo/<int:pk>/', views.DeleteTodoView.as_view(), name='todo-delete'),
    path('edit_todo/<int:pk>/',
         views.EditTodoView.as_view(), name='todo-edit'),
    path('change_status/<int:pk>/',
         views.ChangeStatusView.as_view(), name='change-status'),
    path('search/', views.SearchedTodoView.as_view(), name='search')
]
