# todo_api/serializers.py
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id', 
            'title', 
            'description', 
            'status', 
            'created_at', 
            'updated_at', 
            'due_date', 
            'is_completed'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_status(self, value):
        valid_statuses = ['pending', 'in_progress', 'completed']
        if value not in valid_statuses:
            raise serializers.ValidationError(
                f"Status must be one of: {', '.join(valid_statuses)}"
            )
        return value
    
    def validate(self, data):
        # If status is completed, automatically set is_completed to True
        if data.get('status') == 'completed':
            data['is_completed'] = True
        elif data.get('status') in ['pending', 'in_progress']:
            data['is_completed'] = False
        return data