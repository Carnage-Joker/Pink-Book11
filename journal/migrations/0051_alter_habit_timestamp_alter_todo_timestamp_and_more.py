# Generated by Django 5.0.1 on 2024-05-28 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0050_alter_habit_timestamp_alter_todo_timestamp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 28, 18, 4, 0, 141704)
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 28, 18, 4, 0, 141704)
            ),
        ),
        migrations.AlterField(
            model_name="userfeedback",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 28, 18, 4, 0, 153140)
            ),
        ),
    ]
