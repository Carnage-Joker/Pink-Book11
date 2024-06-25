# Generated by Django 5.0.1 on 2024-06-11 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0079_alter_habit_timestamp_alter_todo_due_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 11, 21, 43, 8, 772405)
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="due_date",
            field=models.DateField(default=datetime.date(2024, 6, 12), null=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 11, 21, 43, 8, 772405)
            ),
        ),
        migrations.AlterField(
            model_name="userfeedback",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 11, 21, 43, 8, 788029)
            ),
        ),
    ]
