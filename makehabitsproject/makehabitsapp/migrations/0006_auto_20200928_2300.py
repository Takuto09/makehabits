# Generated by Django 3.0.4 on 2020-09-28 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makehabitsapp', '0005_auto_20200928_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habitdetailmodel',
            old_name='achievement_date',
            new_name='created_date',
        ),
    ]