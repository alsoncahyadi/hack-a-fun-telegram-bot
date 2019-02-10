from django.shortcuts import render
from django.http import HttpResponse
import requests
import logging
import json
import os
import qrcode
from . import helpers as h
from .replier import Replier
from apple import models

logger = logging.getLogger(__name__)

TOKEN = os.environ['TELE_TOKEN']
replier = Replier(TOKEN)

def chat(request):

    if request.method == "POST" and request.body:
        req_json = json.loads(request.body)
        print(req_json)
        h.escape_if_not_authorized(req_json)
        response = replier.reply(req_json)
        return HttpResponse(response.content)
        
        # message = req_json['message']

        # chat_id = message['chat']['id']
        # key = str(chat_id) + h.generate_salt()
        # qr = qrcode.make(key)
        # caption = "Hello, {} {}!".format(message['from'].get('first_name', ''), message['from'].get('last_name', ''))
        
        # return messenger.send_qr(message, qr, caption)
    else:
        return HttpResponse("Sneaky you!")

def healthz(request):
    return HttpResponse("OK")
