# Generated by Django 4.1.3 on 2022-12-04 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0003_remove_question_answers_answer_question"),
    ]

    operations = [
        migrations.RenameField(
            model_name="answer",
            old_name="is_valid",
            new_name="is_answer",
        ),
    ]
