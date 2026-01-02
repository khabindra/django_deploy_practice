# todo_api/admin.py
from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_completed', 'created_at', 'due_date')
    list_filter = ('status', 'is_completed')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)