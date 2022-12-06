from django.urls import path
from .views import CartsView, CartView, CartsGenerate

urlpatterns = [
    path("", CartsView.as_view(), name="carts_homepage"),
    path("cart/<int:pk>/", CartView.as_view(), name="cart_info"),
    path("cart_range/", CartsGenerate.as_view(), name="cart_generator"),
]
