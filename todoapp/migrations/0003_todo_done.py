# Generated by Django 3.1 on 2022-08-31 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_remove_todo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]