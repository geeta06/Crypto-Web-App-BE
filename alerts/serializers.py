from rest_framework import serializers
from .models import Alert
from decimal import Decimal

class AlertSerializer(serializers.ModelSerializer):
    price_threshold = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Alert
        fields = ['id', 'user', 'cryptocurrency', 'price_threshold', 'above_or_below', 'is_active']
        read_only_fields = ['user']
        
    def validate_price_threshold(self, value):
        try:
            return Decimal(value)
        except (ValueError):
            raise serializers.ValidationError("Invalid price_threshold format.")

    def create(self, validated_data):
        alert = Alert.objects.create(**validated_data)
        return alert