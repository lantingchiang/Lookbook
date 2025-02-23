# frontend/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView

from core.models import Todo


def index(request):
    return render(request, 'frontend/index.html')


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'frontend/index.html'
