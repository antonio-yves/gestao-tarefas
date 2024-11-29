from django.shortcuts import render

# Create your views here.
def list_todos(request):
    return render(request, 'todo/list.html')
