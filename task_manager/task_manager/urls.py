from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # Include task URLs with 'tasks/' prefix
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's auth URLs under 'accounts/'
]
