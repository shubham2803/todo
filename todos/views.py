from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import TodoGetSerializer, TodoCreateSerializer
from .models import Todo


# Create your views here.


class CreateTodo(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoGetSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoGetSerializer


class DeleteTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoGetSerializer
