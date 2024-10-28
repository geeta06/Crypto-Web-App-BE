from cryptocurrency.models import Cryptocurrency
from rest_framework import serializers

class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = "__all__"
