from rest_framework import viewsets, permissions
from rest_framework.response import Response
from cryptocurrency.models import Cryptocurrency
from cryptocurrency.serializers import CryptocurrencySerializer



class CryptocurrencyViewSet(viewsets.ModelViewSet):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    permission_classes = [permissions.IsAuthenticated]
