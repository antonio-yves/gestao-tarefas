from django.urls import path

from .views import *

app_name = 'todo'

urlpatterns = [
    path('', list_todos, name='list_todos'),
]
