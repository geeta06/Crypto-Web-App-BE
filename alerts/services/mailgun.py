

import requests
from crypto_alert_system.settings import ANYMAIL, SENDER_EMAIL, RECIPIENT_EMAIL

def send_email(message, subject=None, email=None):
  	return requests.post(
  		"https://api.mailgun.net/v3/sandboxe8db5ccc8fef48aebcf55bdd985070b8.mailgun.org/messages",
  		auth=("api", ANYMAIL['MAILGUN_API_KEY']),
  		data={"from": SENDER_EMAIL,
  			"to": [RECIPIENT_EMAIL],
  			"subject": subject,
  			"text": message})