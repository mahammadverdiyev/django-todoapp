from django.shortcuts import render, HttpResponseRedirect
from django.utils import timezone
from .models import Todo
from django.urls import reverse
from django.views import View, generic
from django.shortcuts import get_object_or_404


class TodoUtil():
    @classmethod
    def get_todo(self, pk):
        return get_object_or_404(Todo, pk=pk)


class HomeView(generic.ListView):
    template_name = 'todo/home.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.all().order_by('-added_date')


class SearchedTodoView(generic.ListView):
    template_name = 'todo/searched_todo.html'
    context_object_name = 'todos'

    def get_queryset(self):
        searched_todo = self.request.GET['todo_name']
        return Todo.objects.filter(text__startswith=searched_todo).order_by('-added_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['searched_name'] = self.request.GET['todo_name']
        return context


class AddTodoView(View):
    def post(self, request):
        content = request.POST['content']
        Todo.objects.create(added_date=timezone.now(), text=content)
        return HttpResponseRedirect(reverse('todo:todo-home'))


class DeleteTodoView(View):
    def post(self, request, pk):
        todo = TodoUtil.get_todo(pk)
        todo.delete()
        return HttpResponseRedirect(reverse('todo:todo-home'))


class ChangeStatusView(View):
    def get(self, request, pk):
        todo = TodoUtil.get_todo(pk)
        todo.is_done = False if todo.is_done else True
        todo.save()
        return HttpResponseRedirect(reverse('todo:todo-home'))


class EditTodoView(View):
    def post(self, request, pk):
        todo = self.get_todo(pk)
        todo.text = request.POST['content']
        todo.save()
        return HttpResponseRedirect(reverse('todo:todo-home'))

    def get(self, request, pk):
        todo = TodoUtil.get_todo(pk)
        return render(request, 'todo/edit_todo.html', {'todo': todo})
