from django.urls import path
from . import views
# from django.views.generic import TemplateView

app_name = 'polls'

urlpatterns = [
    # path('',
    #      TemplateView.as_view(template_name='polls/index.html'),
    #      name = 'index'
    # ),
    path('', views.ToDoListIndexView.as_view(), name='index'),
    path('list/', views.ToDoListView.as_view(), name='list'),
    path('done/', views.ToDoListDoneView.as_view(), name='done'),
    path('<int:pk>/', views.ToDoDetailView.as_view(), name='detail'),
    path('create/', views.ToDoItemCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.ToDoItemUpdateView.as_view(), name='update'),
    path('<int:pk>/confirm-delete/', views.ToDoItemDeleteView.as_view(), name='delete'),
]
