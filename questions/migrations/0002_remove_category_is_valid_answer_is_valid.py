# Generated by Django 4.1.3 on 2022-12-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="is_valid",
        ),
        migrations.AddField(
            model_name="answer",
            name="is_valid",
            field=models.BooleanField(default=False),
        ),
    ]
