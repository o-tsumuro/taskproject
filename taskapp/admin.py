from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'task_name', 'details', 'date', 'priority')

admin.site.register(Task, TaskAdmin)