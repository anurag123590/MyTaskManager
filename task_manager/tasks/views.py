from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request,'home.html')  



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Get tasks for logged-in user

    # Handle filtering based on completion status
    filter_status = request.GET.get('filter', 'all')
    if filter_status == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_status == 'uncompleted':
        tasks = tasks.filter(completed=False)

    # Handle sorting by due date or completion status
    sort_by = request.GET.get('sort', 'due_date')
    if sort_by == 'due_date':
        tasks = tasks.order_by('due_date')  # Sort by due date
    elif sort_by == 'completed':
        tasks = tasks.order_by('completed')  # Sort by completion status

    return render(request, 'task_list.html', {'tasks': tasks})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})



@login_required
def update_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('tasks:task_list')
