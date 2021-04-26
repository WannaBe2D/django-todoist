from django.urls import path

from . import views


app_name = 'todo'
urlpatterns = [
    path('<int:category_id>/detail/', views.category_detail, name='category_detail'),
    path('create/', views.create_category, name='create_category'),
    path('today_task/', views.today_task, name='today_task'),
    path('future_task/', views.future_task, name='future_task'),
    path('', views.main_page, name='main_view'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('create_task_main/', views.create_task_main, name='create_task_main'),
    path('incoming/', views.incoming_task, name='incoming_task'),
]
