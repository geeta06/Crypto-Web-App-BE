# crypto_alert/tasks.py

from celery import shared_task
from decimal import Decimal
from django.core.mail import send_mail
from .models import Alert
from alerts.services.mailgun import send_email
from cryptocurrency.models import Cryptocurrency

import logging

logger = logging.getLogger(__name__)


def send_crypto_alerts():
    alerts = Alert.objects.filter(is_active=True)
    for alert in alerts:
        currency = Cryptocurrency.objects.filter(
            symbol=alert.cryptocurrency.symbol
        ).first()
        if (alert.above_or_below == 'above' and currency.current_price > alert.price_threshold) or \
           (alert.above_or_below == 'below' and currency.current_price < alert.price_threshold):
            send_alert_email(alert.user.email, alert.cryptocurrency.symbol, currency.current_price)
            alert.is_active = False  # Deactivate after triggering
            alert.save()


def send_alert_email(email, crypto_symbol, price):
    try:
        send_email(
            subject = 'Crypto Price Alert',
            message=f'The price of {crypto_symbol} has reached ${price}.',
            email= [email],
        )
    except Exception as e:
        logger.error(f"Unable to send email due to error {e}")