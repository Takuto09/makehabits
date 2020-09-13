from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import HabitModel
from django.urls import reverse_lazy

class HabitList(ListView):
    template_name = 'habitList.html'
    model = HabitModel

class HabitDetail(DetailView):
    template_name = 'habitDetail.html'
    model = HabitModel

class HabitCreate(CreateView):
    template_name = 'habitCreate.html'
    model = HabitModel
    fields = ('title', 'memo')
    success_url = reverse_lazy('habitList')