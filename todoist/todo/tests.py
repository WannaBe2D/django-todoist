from django.test import TestCase
from django.utils import timezone
import datetime

from .models import Task, Category


class TaskTeasCase(TestCase):
    def setUp(self):
        self.date = timezone.now()

        category = Category.objects.create(category_name='Food')
        Task.objects.create(task_text='Buy milk', pud_date=self.date, category=category)

    def test_create_task(self):
        task = Task.objects.get(task_text='Buy milk')
        category = Category.objects.get(category_name='Food')

        self.assertEqual(task.task_text, 'Buy milk')
        self.assertEqual(task.category, category)
        self.assertEqual(task.pud_date, self.date)

    def test_task_delete(self):
        task = Task.objects.get(pk=1)
        task.delete()
        self.assertEqual(str(Task.objects.all()), "<QuerySet []>")
