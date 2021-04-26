from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.utils import timezone

from .models import Category, Task


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category_list = Category.objects.all()
    return render(request, 'todo/category_detail.html', {'category_list': category_list, 'category_all': category})


def create_category(request):
    if request.method == 'POST':
        category = Category(category_name=request.POST['category'])
        category.save()
        return HttpResponseRedirect(reverse('todo:today_task'))


def create_task(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        task = Task(task_text=request.POST['task'], category=category)
        task.save()
        return HttpResponseRedirect(reverse('todo:category_detail', args=(category_id,)))


def today_task(request):
    task = Task.objects.filter(pud_date__day=datetime.date.today().day)
    category = Category.objects.all()
    context = {'task_list': task, 'category_list': category}
    return render(request, 'todo/today_task.html', context)


def future_task(request):
    task = Task.objects.filter(pud_date__gte=timezone.now() + datetime.timedelta(days=1))
    category = Category.objects.all()
    context = {'task_list': task, 'category_list': category}
    return render(request, 'todo/future_task.html', context)


def main_page(request):
    category = Category.objects.all()
    return render(request, 'todo/index.html', {'category_list': category})


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    category = task.category.id
    task.delete()
    return HttpResponseRedirect(reverse('todo:category_detail', args=(str(category),)))


def create_task_main(request):
    if request.method == 'POST':
        category = Category.objects.get(pk=request.POST.get('category_select'))
        task = Task(task_text=request.POST['task'], category=category, pud_date=request.POST['date_task'] if len(request.POST['date_task']) >= 1 else timezone.now())
        print(request.POST)
        task.save()
        return HttpResponseRedirect(reverse('todo:main_view'))


def incoming_task(request):
    task = Task.objects.all()
    category = Category.objects.all()
    return render(request, 'todo/incoming.html', {'task_list': task, 'category_list': category})
