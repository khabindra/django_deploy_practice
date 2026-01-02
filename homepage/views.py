from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Todo
from .serializers import TodoSerializer

def index(request):
    return render(request, 'homepage/index.html', {})


class TodoListCreateView(generics.ListCreateAPIView):
    """
    View for listing all todos and creating new todos
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a specific todo
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoBulkDeleteView(APIView):
    """
    View for bulk deleting todos
    """
    def delete(self, request):
        todo_ids = request.data.get('ids', [])
        if not todo_ids:
            return Response(
                {'error': 'No todo IDs provided'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        todos = Todo.objects.filter(id__in=todo_ids)
        deleted_count, _ = todos.delete()
        
        return Response(
            {'message': f'{deleted_count} todos deleted successfully'},
            status=status.HTTP_200_OK
        )

class TodoSearchView(generics.ListAPIView):
    """
    View for searching todos
    """
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        queryset = Todo.objects.all()
        
        # Search by title
        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
        
        # Filter by status
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        
        # Filter by completion status
        is_completed = self.request.query_params.get('is_completed', None)
        if is_completed is not None:
            is_completed_bool = is_completed.lower() == 'true'
            queryset = queryset.filter(is_completed=is_completed_bool)
        
        return queryset