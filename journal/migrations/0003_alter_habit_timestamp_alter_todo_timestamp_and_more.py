# Generated by Django 5.0.1 on 2024-03-17 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0002_delete_edittag_remove_tag_timestamp_comment_entry_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 17, 20, 41, 27, 497121)
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 17, 20, 41, 27, 497121)
            ),
        ),
        migrations.AlterField(
            model_name="userfeedback",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 17, 20, 41, 27, 501664)
            ),
        ),
    ]
