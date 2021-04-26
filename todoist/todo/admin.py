from django.contrib import admin

from .models import Category, Task


class CategoryInlines(admin.TabularInline):
    model = Task


class AdminCategory(admin.ModelAdmin):
    inlines = [CategoryInlines]


class AdminTask(admin.ModelAdmin):
    list_display = ['task_text', 'pud_date']
    fields = ('task_text', 'pud_date',)

admin.site.register(Category, AdminCategory)
admin.site.register(Task, AdminTask)
