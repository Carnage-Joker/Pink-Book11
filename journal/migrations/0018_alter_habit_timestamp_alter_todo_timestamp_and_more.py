# Generated by Django 5.0.1 on 2024-04-09 22:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0017_alter_habit_timestamp_alter_todo_due_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 10, 8, 4, 11, 969233)
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 10, 8, 4, 11, 970240)
            ),
        ),
        migrations.AlterField(
            model_name="userfeedback",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 10, 8, 4, 11, 973555)
            ),
        ),
    ]
