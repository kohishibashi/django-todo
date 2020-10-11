from django.urls import path
from django.http import HttpResponse

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sub/', views.sub, name='sub'),
    path('update_page/<int:pk>', views.update, name='update_task'),
]
