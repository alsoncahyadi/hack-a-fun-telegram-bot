from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser, FormParser
from django.db import connection
import requests
import logging
import json
import os
import qrcode
from . import helpers as h
from .replier import Replier
from .messenger import Messenger
from apple import models

TOKEN = os.environ['TELE_TOKEN']
messenger = Messenger(TOKEN)
replier = Replier(messenger)

class Chat(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)
    
    def post(self, request):
        print(h.get_log(request))
        try:
            data = request.data
            if not h.is_message_valid(data):
                return HttpResponse("Sneaky you! You're not authorized!")
            response = replier.reply(data)
            return JsonResponse(json.loads(response.content))
        except:
            return h.error_response(500, "Internal server error", messenger)
        finally:
            connection.close()


def healthz(request):
    return HttpResponse("OK")
