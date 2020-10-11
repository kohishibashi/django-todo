from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


def home(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'kiritan/top.html', context)


def sub(request):
    return render(request, 'kiritan/sub.html')


def update(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }

    return render(request, 'kiritan/update_page.html', context)
