# Generated by Django 4.1.3 on 2022-12-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_cart", models.CharField(max_length=12)),
                ("date_registration", models.DateTimeField(auto_now=True)),
                ("date_end", models.DateTimeField()),
            ],
        ),
    ]