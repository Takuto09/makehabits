import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  View)
from django.utils import timezone

from .forms import LoginForm, UserCreateForm
from .models import AchievesModel, HabitModel


class HabitList(LoginRequiredMixin, ListView):
    template_name = 'habitList.html'
    model = HabitModel

    def get_queryset(self):
        today_min = datetime.datetime.combine(
            datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(
            datetime.date.today(), datetime.time.max)
        today_achieves = Count('achievesmodel', filter=Q(
            achievesmodel__created_date__range=(today_min, today_max)))
        queryset = HabitModel.objects.filter(
            user_id=self.request.user.id).annotate(achieves=today_achieves)
        return queryset


class HabitDetail(DetailView):
    template_name = 'habitDetail.html'
    model = HabitModel


class HabitCreate(CreateView):
    template_name = 'habitCreate.html'
    model = HabitModel
    fields = ('title', 'memo')
    success_url = reverse_lazy('habitList')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user_id = self.request.user.id
        obj.save()
        return redirect(self.success_url)


class HabitUpdate(UpdateView):
    template_name = 'habitUpdate.html'
    model = HabitModel
    fields = ('title', 'memo')
    success_url = reverse_lazy('habitList')


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


def achievefunc(request, pk):
    post = HabitModel.objects.get(pk=pk)

    # key情報(id、日付)のデータを取得
    today_min = datetime.datetime.combine(
        datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(
        datetime.date.today(), datetime.time.max)
    achieves = AchievesModel.objects.filter(
        habit__id=post.id, created_date__range=(today_min, today_max))

    if achieves.count() == 0:
        # データが存在しない場合、新規作成
        new_achieve = AchievesModel()
        new_achieve.habit = post
        new_achieve.save()
    else:
        # データが存在する場合、削除
        achieves.delete()
    return redirect('/habitList')
