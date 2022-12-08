from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import CartApiView

router = DefaultRouter()
router.register("cart", CartApiView, basename="cart")

urlpatterns = [path("", include(router.urls))]
