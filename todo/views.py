from django.shortcuts import render, HttpResponseRedirect
from django.utils import timezone
from .models import Todo
from django.urls import reverse


def home(request):
    todos = Todo.objects.all().order_by("-added_date")
    return render(request, 'todo/home.html', {'todos': todos})


def add_todo(request):
    added_date = timezone.now()
    content = request.POST['content']
    Todo.objects.create(added_date=added_date, text=content)
    return HttpResponseRedirect(reverse('todo:todo-home'))


def delete_todo(request, todo_id):
    if request.method == 'POST':
        Todo.objects.get(id=todo_id).delete()
        return HttpResponseRedirect(reverse('todo:todo-home'))


def change_status(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    todo.is_done = False if todo.is_done else True

    todo.save()

    return HttpResponseRedirect(reverse('todo:todo-home'))


def edit_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.text = request.POST['content']
        todo.save()
        return HttpResponseRedirect(reverse('todo:todo-home'))

    return render(request, 'todo/edit_todo.html', {'todo': todo})
