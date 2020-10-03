from django.urls import path
from .views import HabitList, HabitDetail, HabitCreate, HabitUpdate, Account_login, Create_account, logoutfunc, achievefunc

urlpatterns = [
    path('habitList/', HabitList.as_view(), name='habitList'),
    path('achieve/<int:pk>', achievefunc, name='achieve'),
    path('habitDetail/<int:pk>', HabitDetail.as_view(), name='habitDetail'),
    path('habitCreate/', HabitCreate.as_view(), name='habitCreate'),
    path('habitUpdate/<int:pk>', HabitUpdate.as_view(), name='habitUpdate'),
    path('signup/', Create_account.as_view(), name='signup'),
    path('login/', Account_login.as_view(), name='login'),
    path('logout/', logoutfunc, name='logout'),
]
