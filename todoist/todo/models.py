from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=450)

    def __str__(self):
        return self.category_name


class Task(models.Model):
    task_text = models.CharField(max_length=450)
    pud_date = models.DateTimeField(default=timezone.now())
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_text
