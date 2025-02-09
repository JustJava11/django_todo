from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import ToDoItem


# def index_view(request: HttpRequest) -> HttpResponse:
#     todo_items = ToDoItem.objects.all()
#     return render(request,
#                   template_name='polls/index.html',
#                   context={'todo_items': todo_items[:3]})


class ToDoListIndexView(ListView):
    template_name = 'polls/index.html'
    queryset = ToDoItem.objects.all()[:5]


class ToDoListView(ListView):
    model = ToDoItem
