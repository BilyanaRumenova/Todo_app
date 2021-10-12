from django.urls import path

from todo_app.accounts.views import register, login_user, logout_user

urlpatterns = (
    path('signup/', register, name='register'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
)
