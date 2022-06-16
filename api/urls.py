from django.urls import path
from . import views


urlpatterns = [
    path('vololo/', views.getData),
    path('task/', views.taskList, name='task-list'),
    path('task-create/', views.taskCreate, name ='task-create')
]