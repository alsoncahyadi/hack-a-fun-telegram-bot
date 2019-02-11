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

TOKEN = os.environ['TELE_TOKEN']
replier = Replier(TOKEN)

def chat(request):
    print(h.get_log(request))
    if request.method == "POST" and h.is_authorized(request):
        req_json = json.loads(request.body)
        if not h.is_message_valid(req_json):
            return HttpResponse("Sneaky you! You're not authorized!")
        response = replier.reply(req_json)
        return HttpResponse(response.content)
    else:
        return HttpResponse("Sneaky you!")

def healthz(request):
    return HttpResponse("OK")
