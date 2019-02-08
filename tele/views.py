from django.shortcuts import render
from django.http import HttpResponse
import requests
import logging
import json
import os
import qrcode
from . import helpers as h
from io import BytesIO

logger = logging.getLogger(__name__)

TOKEN = os.environ['TELE_TOKEN']
TELEGRAM_REQUEST_URL = "https://api.telegram.org/bot{token}/{method}"
TELEGRAM_GET_URL = TELEGRAM_REQUEST_URL + "?chat_id={chat_id}&text={text}"

def chat(request):
    if request.method == "POST" and request.body:
        req_json = json.loads(request.body)
        print(req_json)
        
        message = req_json['message']
        chat_id = message['chat']['id']

        key = str(chat_id) + h.generate_salt()

        qr = qrcode.make(key)
        byte_io = BytesIO()
        qr.save(byte_io, 'png')
        byte_io.seek(0)

        print(TELEGRAM_REQUEST_URL.format(token=TOKEN, method='sendPhoto'))
        return HttpResponse(
            requests.post(TELEGRAM_REQUEST_URL.format(token=TOKEN, method='sendPhoto'), 
                data={
                    'chat_id': chat_id,
                    'caption': "Hello, {} {}!".format(message['from'].get('first_name', ''), message['from'].get('last_name', ''))
                },
                files={
                    'photo': (
                        'qr.png',
                        byte_io,
                        'image/png'
                    )
                }
            ).content
        )
    else:
        return HttpResponse("Sneaky you!")

def healthz(request):
    return HttpResponse("OK")