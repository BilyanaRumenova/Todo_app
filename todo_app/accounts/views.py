from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'GET':
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'todo/register.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current todos')
            except IntegrityError:
                context = {
                    'form': UserCreationForm(),
                    'error': 'That username has already been taken. Please choose a new username',
                }
                return render(request, 'todo/register.html', context)
        else:
            context = {
                'form': UserCreationForm(),
                'error': 'Passwords did not match',
            }
            return render(request, 'todo/register.html', context)


def login_user(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm()
        }
        return render(request, 'todo/login_user.html', context)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context = {
                'form': AuthenticationForm(),
                'error': 'Username and password did not match'
            }
            return render(request, 'todo/login_user.html', context)
        else:
            login(request, user)
            return redirect('current todos')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
