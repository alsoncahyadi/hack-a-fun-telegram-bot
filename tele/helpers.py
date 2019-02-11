from django.http import HttpResponse
import random
import os
import json

def generate_salt(n=16):
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars=[]
    for i in range(n):
        chars.append(random.choice(ALPHABET))

    
    return "".join(chars)

def is_message_valid(req_json):
    try:
        if req_json['message']['from']['is_bot']:
            return False
    except:
        return False

    return True

def is_authorized(request):
    return (request.body and request.get_host() == '') or os.environ.get('IS_PRODUCTION') != 'TRUE'

def get_log(request):
    log_entries = {
        'agent': request.META.get('HTTP_USER_AGENT', ''),
        'remote_host': ' | '.join([request.META.get('REMOTE_ADDR'), request.META.get('HTTP_ORIGIN', '')]),
        'body': request.body,
    }
    log_entries_list = ["'{k}': '{v}'".format(k=k, v=v) for k, v in log_entries.items()]
    return "{ " + "; ".join(log_entries_list) + " }"

def error_response(code, message):
    message_entry = json.dumps({
        'code': code,
        'message': message
    })
    return HttpResponse(message_entry, status=code)

def game_type_to_i(game_type_s):
    return {
        'physical_game': 1,
        'ctr_tournament': 2,
        'ctr_free_play': 3,
        'cerdas_cermat': 4,
        'ranking_1': 5,
        'guitar_hero': 6,
        'cs_go': 7,
        'winning_eleven': 8,
    }.get(game_type_s, None)

def game_type_to_s(game_type_i):
    return {
        1: 'physical_game',
        2: 'ctr_tournament',
        3: 'ctr_free_play',
        4: 'cerdas_cermat',
        5: 'ranking_1',
        6: 'guitar_hero',
        7: 'cs_go',
        8: 'winning_eleven',
    }.get(game_type_i, None)