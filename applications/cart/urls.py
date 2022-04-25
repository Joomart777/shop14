from rest_framework.routers import DefaultRouter

from applications.cart.views import CartViewSet

router = DefaultRouter()
router.register('', CartViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)