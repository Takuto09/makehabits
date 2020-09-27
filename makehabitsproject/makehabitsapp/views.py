from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, View

from .forms import LoginForm, UserCreateForm
from .models import HabitModel


class HabitList(LoginRequiredMixin, ListView):
    template_name = 'habitList.html'
    model = HabitModel

    def get_queryset(self):
        return HabitModel.objects.filter(user_id=self.request.user.id)


class HabitDetail(DetailView):
    template_name = 'habitDetail.html'
    model = HabitModel


class HabitCreate(CreateView):
    template_name = 'habitCreate.html'
    model = HabitModel
    fields = ('title', 'memo')
    success_url = reverse_lazy('habitList')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = self.request.user.id
            obj.save()
            return super().post(request, *args, **kwargs)


class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            # フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            # フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/habitList')
        else:
            return render(request, 'signup.html', {'form': form, })

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'signup.html', {'form': form, })


create_account = Create_account.as_view()


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


def logoutfunc(request):
    logout(request)
    return redirect('login')
