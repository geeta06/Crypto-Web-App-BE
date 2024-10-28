from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cryptocurrency.views import CryptocurrencyViewSet

router = DefaultRouter()
router.register('cryptocurrencies', CryptocurrencyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
