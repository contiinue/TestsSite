from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import GenericViewSet

from carts.models import Cart
from .serializers import CartSerializer


class CartApiView(GenericViewSet, UpdateAPIView, DestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
