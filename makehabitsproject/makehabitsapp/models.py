from django.db import models


class HabitModel(models.Model):
    # 登録する習慣の内容
    habit_id = models.CharField(max_length=100, default='0', auto_created=True)
    user_id = models.CharField(max_length=100, default='0')
    title = models.CharField(max_length=100)
    memo = models.TextField()

    def __str__(self):
        return self.title


class AchievesModel(models.Model):
    # 登録する習慣の実績
    habit = models.ForeignKey(
        HabitModel, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.habit.habit_id
