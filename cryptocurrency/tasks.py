# crypto_alert/tasks.py

from celery import shared_task
from decimal import Decimal
from alerts.price_data import get_all_crypto_prices
from .models import Cryptocurrency
from alerts.tasks import send_crypto_alerts

import logging

logger = logging.getLogger(__name__)

@shared_task
def update_crypto_prices():
    try:
        crypto_data = get_all_crypto_prices()
        for data in crypto_data:
            payload = {
                "name": data.get('name'),
                "symbol": data.get('symbol').upper(),
                "current_price": data.get('current_price'),
                "image": data.get('image'),
                "total_volume": data.get('total_volume'),
                "high_24h": data.get('high_24h'),
                "low_24h": data.get('low_24h')
            }
            #update cryptocurrencies
            Cryptocurrency.objects.filter(name=data.get('name')).update(**payload) 
        send_crypto_alerts()
    except Exception as e:
        logger.error(msg=f"Unable to update price due to error {e}")