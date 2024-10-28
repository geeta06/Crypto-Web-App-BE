# token_metrics_app/views.py
import requests
from django.http import JsonResponse
from django.conf import settings
from crypto_alert_system.settings import BASEURL
from crypto_alert_system.settings import COINGEIKO_BASEURL


def get_all_crypto_prices():
    
    url =  f"{COINGEIKO_BASEURL}/api/v3/coins/markets?vs_currency=usd"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'error': 'Failed to fetch data'}
