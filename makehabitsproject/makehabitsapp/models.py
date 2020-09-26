from django.db import models


class HabitModel(models.Model):
    user_id = models.CharField(max_length=100, default='0')
    title = models.CharField(max_length=100)
    memo = models.TextField()

    def __str__(self):
        return self.title
