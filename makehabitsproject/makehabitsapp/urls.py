from django.urls import path
from .views import HabitList, HabitDetail, HabitCreate, Account_login, Create_account

urlpatterns = [
    path('habitList/', HabitList.as_view(), name='habitList'),
    path('habitDetail/<int:pk>', HabitDetail.as_view(), name='habitDetail'),
    path('habitCreate/', HabitCreate.as_view(), name='habitCreate'),
    path('signup/', Create_account.as_view(), name='signup'),
    path('login/', Account_login.as_view(), name='login'),
]
