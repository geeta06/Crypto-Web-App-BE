from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from cryptocurrency.models import Cryptocurrency

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    price_threshold = models.DecimalField(max_digits=10, decimal_places=2)
    above_or_below = models.CharField(max_length=5, choices=[('above', 'Above'), ('below', 'Below')])
    is_active = models.BooleanField(default=True)
    email_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} alert for {self.cryptocurrency.name}"

