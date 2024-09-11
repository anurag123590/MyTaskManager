from django.urls import path
from . import views

app_name= 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),  
    path('create/', views.create_task, name='create_task'),  # This will be mapped to 'tasks/create/'
    path('<int:task_id>/update/', views.update_task, name='update_task'),  # This will be mapped to 'tasks/<task_id>/update/'
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),  # This will be mapped to 'tasks/<task_id>/delete/'
    path('signup/', views.signup, name='signup'),
    ]
