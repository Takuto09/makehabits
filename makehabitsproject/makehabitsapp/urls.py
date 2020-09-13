from django.urls import path
from .views import HabitList, HabitDetail, HabitCreate

urlpatterns = [
    path('habitList/', HabitList.as_view(), name='habitList'),
    path('habitDetail/<int:pk>', HabitDetail.as_view(), name='habitDetail'),
    path('habitCreate/', HabitCreate.as_view(), name='habitCreate'),
]
