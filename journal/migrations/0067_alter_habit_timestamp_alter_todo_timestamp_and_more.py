# Generated by Django 5.0.1 on 2024-06-03 02:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0066_alter_habit_timestamp_alter_todo_due_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 3, 12, 23, 48, 319435)
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 3, 12, 23, 48, 319435)
            ),
        ),
        migrations.AlterField(
            model_name="userfeedback",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 3, 12, 23, 48, 319435)
            ),
        ),
    ]
