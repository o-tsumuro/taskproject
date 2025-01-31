from django.urls import path
from . import views

app_name = 'taskapp'

urlpatterns = [
    path('', views.FormAndListView.as_view(), name='index'),
    path('task/<int:pk>/detail/', views.task_detail, name='task_detail'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    ]