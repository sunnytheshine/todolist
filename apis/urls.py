from django.urls import path

from .views import ListTodo, DetailTodo

urlpatterns = [
    path('', ListTodo, name='ListTodo'),
    path('<int:pk>/', DetailTodo, name='DetailTodo'),
]