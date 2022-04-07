from rest_framework import serializers

from .models import Todo


class TodoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'task_id',
            'user',
            'task_title',
            'task_description',
            'task_state',
            'task_due_date',
        )


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'user',
            'task_title',
            'task_description',
            'task_state',
            'task_due_date',
        )
