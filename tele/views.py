from django.shortcuts import render
from django.http import HttpResponse
import logging
import json

logger = logging.getLogger(__name__)

# Create your views here.
def chat(request):
    if request.method == "POST":
        params = json.loads(request.body)
        print(params)
        return HttpResponse("HI!")
    else:
        return HttpResponse("Sneaky you!")

def healthz(request):
    return HttpResponse("OK")