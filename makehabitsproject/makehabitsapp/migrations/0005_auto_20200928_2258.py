# Generated by Django 3.0.4 on 2020-09-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makehabitsapp', '0004_habitmodel_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='HabitDetailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('habit_id', models.CharField(max_length=100)),
                ('achievement_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='habitmodel',
            name='habit_id',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
