from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'kiritan/top.html')


def sub(request):
    return render(request, 'kiritan/sub.html')
