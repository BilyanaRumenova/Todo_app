from django.urls import path

from todo_app.todo.views import home, create_todo, current_todos, completed_todos, view_todo, complete_todo, delete_todo

urlpatterns = (
    path('', home, name='home'),
    path('create/', create_todo, name='create todo'),
    path('current/', current_todos, name='current todos'),
    path('completed/', completed_todos, name='completed todos'),
    path('todo/<int:todo_pk>', view_todo, name='view todo'),
    path('todo/<int:todo_pk>/complete', complete_todo, name='complete todo'),
    path('todo/<int:todo_pk>/delete', delete_todo, name='delete todo'),
)
