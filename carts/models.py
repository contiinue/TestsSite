from django.db import models
from django.utils import timezone


class Payment(models.Model):
    pay = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)

    def __str__(self):
        return f"Date-payment:{self.date} - Pay: {self.pay}$"


class Cart(models.Model):
    number_cart = models.CharField(max_length=12, unique=True)
    date_registration = models.DateTimeField(auto_now=True)
    date_end = models.DateTimeField()

    def __str__(self):
        return self.number_cart

    def status_cart(self) -> bool:
        return self.date_end > timezone.now()
