from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import ToDoItem

def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.order_by('id').all()
    return render(request,
                  template_name='polls/index.html',
                  context={'todo_items': todo_items})
