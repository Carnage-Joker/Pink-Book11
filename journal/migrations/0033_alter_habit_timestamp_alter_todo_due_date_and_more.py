# Generated by Django 5.0.1 on 2024-05-21 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0032_alter_habit_timestamp_alter_todo_due_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 22, 4, 15, 41, 504740)
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="due_date",
            field=models.DateField(default=datetime.date(2024, 5, 23), null=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 22, 4, 15, 41, 505741)
            ),
        ),
        migrations.AlterField(
            model_name="userfeedback",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 22, 4, 15, 41, 514952)
            ),
        ),
    ]
