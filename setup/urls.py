
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from todos.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoFinishView, register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TodoListView.as_view(), name='list'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name='delete'),
    path('finish/<int:pk>', TodoFinishView.as_view(), name='finish'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='todos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
