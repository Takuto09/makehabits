# Generated by Django 3.0.4 on 2020-10-02 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makehabitsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitmodel',
            name='achieve',
            field=models.BooleanField(null=True),
        ),
    ]