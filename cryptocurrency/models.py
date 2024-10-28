from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=400, blank=True)
    total_volume = models.FloatField(default=0)
    high_24h = models.FloatField(default=0)
    low_24h = models.FloatField(default=0)

    def __str__(self):
        return self.name