from django.db import models
from accounts.models import CustomUser

class Task(models.Model):
    
    class Priority(models.IntegerChoices):
        LOWEST = 1, "1(Lowest)"
        LOW = 2, "2(Low)"
        MEDIUM = 3, "3(middle)"
        HIGH = 4, "4(High)"
        HIGHEST = 5, "5(Highest)"

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        )
    
    task_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        )
    
    details = models.TextField()
    
    date = models.DateField()
    
    priority = models.IntegerField(
        choices=Priority.choices,
        default=Priority.MEDIUM,
        )
    
    def __str__(self):
        return self.task_name