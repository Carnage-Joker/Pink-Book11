# Generated by Django 5.0.1 on 2024-06-23 01:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0092_alter_habit_timestamp_alter_todo_due_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="journalentry",
            name="prompt",
        ),
        migrations.AddField(
            model_name="journalentry",
            name="prompt_text",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="habit",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 23, 11, 10, 56, 956657)
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="due_date",
            field=models.DateField(default=datetime.date(2024, 6, 24), null=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 23, 11, 10, 56, 956657)
            ),
        ),
        migrations.AlterField(
            model_name="userfeedback",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 23, 11, 10, 56, 961164)
            ),
        ),
        migrations.DeleteModel(
            name="Insight",
        ),
        migrations.DeleteModel(
            name="JournalPrompt",
        ),
    ]
