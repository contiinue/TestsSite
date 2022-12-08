# Generated by Django 4.1.3 on 2022-12-07 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carts", "0002_alter_cart_number_cart_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="status",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="payment",
            name="date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]