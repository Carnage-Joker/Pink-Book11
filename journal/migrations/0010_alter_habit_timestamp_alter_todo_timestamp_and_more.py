# Generated by Django 5.0.1 on 2024-03-19 07:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0009_alter_habit_timestamp_alter_todo_due_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 19, 18, 13, 28, 59299)
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 19, 18, 13, 28, 59299)
            ),
        ),
        migrations.AlterField(
            model_name="userfeedback",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 19, 18, 13, 28, 67778)
            ),
        ),
    ]
