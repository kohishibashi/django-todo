from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def home(request):
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
    }
    return render(request, 'kiritan/top.html', context)


def sub(request):
    return render(request, 'kiritan/sub.html')
