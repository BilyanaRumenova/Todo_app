from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'todo/home.html')


@login_required
def create_todo(request):
    if request.method == 'GET':
        context = {
            'form': TodoForm()
        }
        return render(request, 'todo/create_todo.html', context)
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('current todos')
        except ValueError:
            context = {
                'form': TodoForm(),
                'error': 'Bad data passed in. Try again.',
            }
            return render(request, 'todo/create_todo.html', context)


@login_required
def current_todos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    context = {
        'todos': todos,
    }
    return render(request, 'todo/current_todos.html', context)


@login_required
def completed_todos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    context = {
        'todos': todos,
    }
    return render(request, 'todo/completed_todos.html', context)


@login_required
def view_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        context = {
            'todo': todo,
            'form': form,
        }
        return render(request, 'todo/view_todo.html', context)
    else:
        form = TodoForm(request.POST, instance=todo)
        try:
            form.save()
            return redirect('current todos')
        except ValueError:
            context = {
                'todo': todo,
                'form': form,
                'error': 'Bad info',
            }
            return render(request, 'todo/view_todo.html', context)


@login_required
def complete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('current todos')


@login_required
def delete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('current todos')
