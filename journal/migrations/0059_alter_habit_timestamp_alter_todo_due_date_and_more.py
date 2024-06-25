# Generated by Django 5.0.1 on 2024-05-30 23:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0058_alter_habit_timestamp_alter_todo_timestamp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 31, 9, 46, 12, 177120)
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="due_date",
            field=models.DateField(default=datetime.date(2024, 6, 1), null=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 31, 9, 46, 12, 177120)
            ),
        ),
        migrations.AlterField(
            model_name="userfeedback",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 31, 9, 46, 12, 181824)
            ),
        ),
    ]
