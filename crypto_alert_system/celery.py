# crypto_alert/celery.py
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_alert_system.settings')
app = Celery('crypto_alert_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()  # This discovers tasks in installed Django apps
app.conf.broker_connection_retry_on_startup = True

app.conf.beat_schedule = {
    'update_crypto_prices': {
        'task': 'cryptocurrency.tasks.update_crypto_prices',
        'schedule': crontab(minute='*/10'),  # Every 10 minutes
    },
}
