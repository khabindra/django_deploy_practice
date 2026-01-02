from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('todos/', views.TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', views.TodoRetrieveUpdateDestroyView.as_view(), 
         name='todo-detail'),
    
    # Bulk operations
    path('todos/bulk-delete/', views.TodoBulkDeleteView.as_view(), 
         name='todo-bulk-delete'),
    
    # Search and filter
    path('todos/search/', views.TodoSearchView.as_view(), name='todo-search'),
]