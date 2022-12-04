# Generated by Django 4.1.3 on 2022-12-04 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0002_remove_category_is_valid_answer_is_valid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="answers",
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="questions.question",
            ),
            preserve_default=False,
        ),
    ]
