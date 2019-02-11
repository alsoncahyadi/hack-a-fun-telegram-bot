from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
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

class Chat(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        req_json = json.loads(request.body)
        if not h.is_message_valid(req_json):
            return HttpResponse("Sneaky you! You're not authorized!")
        response = replier.reply(req_json)
        return HttpResponse(response.content)


def healthz(request):
    return HttpResponse("OK")
