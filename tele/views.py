from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser, FormParser
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
    parser_classes = (JSONParser)
    
    def post(self, request):
        print(h.get_log(request))
        data = request.data
        if not h.is_message_valid(data):
            return HttpResponse("Sneaky you! You're not authorized!")
        response = replier.reply(data)
        return HttpResponse(response.content)


def healthz(request):
    return HttpResponse("OK")
