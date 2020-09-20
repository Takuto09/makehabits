from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, View
from .models import HabitModel
from django.urls import reverse_lazy
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


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


class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/habitList')
        else:
            return render(request, 'login.html', {'form': form, })

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form, })


account_login = Account_login.as_view()
