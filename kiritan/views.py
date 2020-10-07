from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('ほーむ')


def sub(request):
    return HttpResponse('さぶぺーじ')
