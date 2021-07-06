from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegistrationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('todo:todo-home')
        messages.error(
            request, 'Unsuccessful registration. Invalid information.')
        return render(request, 'users/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("todo:todo-home")
            else:
                messages.error(request, "Invalid username or password")

        else:
            messages.error(request, "Invalid username or password")
        return render(request, 'users/login.html', {'form': form})
