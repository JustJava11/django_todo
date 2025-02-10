from django.contrib import admin
from polls.models import ToDoItem


@admin.register(ToDoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = 'id','title', 'description', 'done'
    list_display_links = 'id', 'title'
