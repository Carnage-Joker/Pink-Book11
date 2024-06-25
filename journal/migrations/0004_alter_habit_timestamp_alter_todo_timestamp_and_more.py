# Generated by Django 5.0.1 on 2024-03-17 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0003_alter_habit_timestamp_alter_todo_timestamp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 17, 20, 49, 19, 618260)
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 17, 20, 49, 19, 618260)
            ),
        ),
        migrations.AlterField(
            model_name="userfeedback",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 17, 20, 49, 19, 623260)
            ),
        ),
    ]
