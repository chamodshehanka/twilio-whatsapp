import os
from twilio.rest import Client

client = Client()

from_whatsapp_number='whatsapp:+'
to_whatsapp_number='whatsapp:' + os.environ['MY_PHONE']
