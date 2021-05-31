from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='todo-home'),
    path('add_todo/', views.add_todo, name='todo-add'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='todo-delete'),
    path('edit_todo/<int:todo_id>/', views.edit_todo, name='todo-edit'),
    path('change_status/<int:todo_id>/',
         views.change_status, name='change-status')
]
