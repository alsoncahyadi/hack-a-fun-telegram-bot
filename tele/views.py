from django.shortcuts import render
from django.http import HttpResponse
import requests
import logging
import json
import os

logger = logging.getLogger(__name__)

TOKEN = os.environ['TELE_TOKEN']
TELEGRAM_REQUEST_URL = "https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"

# Create your views here.
def chat(request):
    if request.method == "POST" and request.body:
        req_json = json.loads(request.body)
        print(req_json)
        
        message = req_json['message']
        chat_id = message['chat']['id']
        return HttpResponse(
            requests.get(TELEGRAM_REQUEST_URL.format(
                token=TOKEN,
                chat_id=chat_id,
                text="Hello, {} {}!".format(message['from'].get('first_name', ''), message['from'].get('last_name', ''))
            )).content
        )
    else:
        return HttpResponse("Sneaky you!")

def healthz(request):
    return HttpResponse("OK")