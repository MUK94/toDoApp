from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from . forms import LoginForm

app_name = 'todoApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='todoApp/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('todo/new/', views.createTodo, name='createTodo'),
    path('todo/<int:pk>/edit/', views.editTodo, name='editTodo'),
    path('todo/<int:pk>/delete/', views.deleteTodo, name='deleteTodo'),
]