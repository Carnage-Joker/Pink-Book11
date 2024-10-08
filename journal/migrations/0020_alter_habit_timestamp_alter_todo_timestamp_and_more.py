# Generated by Django 5.0.1 on 2024-04-09 23:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0019_alter_habit_timestamp_alter_todo_timestamp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 10, 9, 14, 27, 537182)
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 10, 9, 14, 27, 538289)
            ),
        ),
        migrations.AlterField(
            model_name="userfeedback",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 10, 9, 14, 27, 542183)
            ),
        ),
    ]
