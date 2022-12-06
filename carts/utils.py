from .models import Cart
import random


def cart_ranger(date_end, count_range: int) -> None:
    for i in range(count_range):
        model = Cart.objects.create(
            date_end=date_end, number_cart="".join(random.sample("123456789101112", 12))
        )
        model.save()
