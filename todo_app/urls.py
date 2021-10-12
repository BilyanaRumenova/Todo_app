from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.todo.urls')),
    path('accounts/', include('todo_app.accounts.urls')),
    path('api/', include('todo_app.todo_api.urls')),
]
