from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import TaskList
from .forms import TaskForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def todolist(request):
    if request.method=="POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage=request.user
            instance.save()
            messages.success(request,'New Task Added')
        return redirect('todolist')
    else:
        all_tasks=TaskList.objects.filter(manage=request.user)
        paginator=Paginator(all_tasks,5)
        page_num=request.GET.get('pg')
        all_tasks=paginator.get_page(page_num)
        context={'welcome':'Welcome to TodoList Page',                
                'all_tasks':all_tasks}
        return render(request,'todolist.html',context)
@login_required
def delete(request,task_id):  
    task_obj=TaskList.objects.get(pk=task_id)
    if task_obj.manage==request.user:
        task_obj.delete()
        return redirect('todolist')
    else:
        return redirect('login')
@login_required
def edit(request,task_id):
    task_obj=TaskList.objects.get(pk=task_id)
    if request.method=="POST":
        form=TaskForm(request.POST, instance=task_obj)
        if form.is_valid():
            form.save()
            messages.success(request,'Task Editted')
        return redirect('todolist')
    else:       
        context={'welcome':'Welcome to TodoList Page',
                'task_obj':task_obj}
        return render(request,'edit.html',context)
@login_required
def completed(request,task_id):
    task_obj=TaskList.objects.get(pk=task_id)
    if task_obj.manage==request.user:
        task_obj.done=True
        task_obj.save()
    else:
        messages.error(request,'Action is not allowed')
    return redirect('todolist')
@login_required
def incompleted(request,task_id):
    task_obj=TaskList.objects.get(pk=task_id)
    if task_obj.manage==request.user:    
        task_obj.done=False
        task_obj.save()
    else:
        messages.error(request,'Action is not allowed')
    return redirect('todolist')
def home(request):    
    return render(request,'home.html')
def contact(request):
    context={'welcome':'Welcome to Contact Us Page'}
    return render(request,'contact.html',context)
def about(request):
    context={'welcome':'Welcome to About Us Page'}
    return render(request,'about.html',context)