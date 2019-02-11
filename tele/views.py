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
        if not h.is_authorized(req_json):
            return HttpResponse("Sneaky you! You're not authorized!")
        response = replier.reply(req_json)
        return HttpResponse(response.content)
    else:
        return HttpResponse("Sneaky you!")

def healthz(request):
    return HttpResponse("OK")
