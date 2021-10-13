from django.urls import path

from todo_app.todo_api.views import TodoCompletedList, TodoListCreate, TodoRetrieveUpdateDestroy, TodoComplete, \
    register, log_in

urlpatterns = (
    path('todos/', TodoListCreate.as_view()),
    path('todos/<int:pk>', TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', TodoComplete.as_view()),
    path('todos/completed', TodoCompletedList.as_view()),

    path('register', register),
    path('login', log_in),
)