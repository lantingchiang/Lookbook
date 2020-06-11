# core/api/views.py

from rest_framework import viewsets

from .serializers import TodoSerializer
from core.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer