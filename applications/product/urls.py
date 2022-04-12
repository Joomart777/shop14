from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.product.views import *

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # path('', ListCreateView.as_view()),
    # path('<int:pk>/', DeleteUpdateRetriveView.as_view())
]