# Generated by Django 5.0.1 on 2024-05-25 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0038_alter_habit_timestamp_alter_todo_due_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="failed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="todo",
            name="penalty_issued",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="habit",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 25, 19, 16, 25, 81385)
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 25, 19, 16, 25, 81385)
            ),
        ),
        migrations.AlterField(
            model_name="userfeedback",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 25, 19, 16, 25, 86468)
            ),
        ),
    ]
