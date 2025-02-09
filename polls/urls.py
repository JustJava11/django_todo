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
]
