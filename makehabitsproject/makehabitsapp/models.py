from django.db import models


class AchievesModel(models.Model):
    # 登録する習慣の実績
    user_id = models.CharField(max_length=100)
    habit_id = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_id + '_' + self.habit_id


class HabitModel(models.Model):
    # 登録する習慣の内容
    user_id = models.CharField(max_length=100, default='0')
    habit_id = models.CharField(max_length=100, default='0')
    title = models.CharField(max_length=100)
    memo = models.TextField()
    achieve = models.BooleanField(null=True)
    # achieves = models.ManyToManyField(
    #     AchievesModel, related_name='habit_2_achieves')


def __str__(self):
    return self.title
