from django.urls import reverse_lazy

from .models import ToDoItem
from .forms import ToDoItemCreateForm, ToDoItemUpdateForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


# def index_view(request: HttpRequest) -> HttpResponse:
#     todo_items = ToDoItem.objects.all()
#     return render(request,
#                   template_name='polls/index.html',
#                   context={'todo_items': todo_items[:3]})


class ToDoListIndexView(ListView):
    template_name = 'polls/index.html'
    queryset = ToDoItem.objects.all()[:5]


class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=False).all()


class ToDoListView(ListView):
    model = ToDoItem


class ToDoDetailView(DetailView):
    model = ToDoItem

class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemCreateForm
    # fields = ('title', 'description',)

class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    form_class = ToDoItemUpdateForm
     # fields = ('title',
    #           'description',
    #           'done')

class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    success_url = reverse_lazy('polls:list')