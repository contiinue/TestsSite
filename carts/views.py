from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from .forms import GenerateCartForm
from .models import Cart
from .utils import cart_ranger


class CartsView(ListView):
    template_name = "carts/carts.html"
    queryset = Cart.objects.all().order_by("number_cart")
    context_object_name = "carts"


class CartView(DetailView):
    template_name = "carts/cart.html"
    model = Cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["history_payment"] = context["cart"].payment_set.all()
        return context


class CartsGenerate(FormView):
    template_name = "carts/carts_generate.html"
    form_class = GenerateCartForm
    success_url = reverse_lazy("carts_homepage")

    def form_valid(self, form):
        date_end, count_range_cart = (
            form.cleaned_data["date_end_cart"],
            form.cleaned_data["count_renge_cart"],
        )
        cart_ranger(date_end, count_range_cart)
        return super().form_valid(form)
