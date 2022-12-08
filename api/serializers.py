from rest_framework.serializers import ModelSerializer
from carts.models import Cart


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        read_only_fields = ["number_cart", "date_registration", "date_end"]
