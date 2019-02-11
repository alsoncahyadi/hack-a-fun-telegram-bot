import random
import os

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
        'host': request.META.get('HTTP_HOST', ''),
        'body': request.body,
    }
    log_entries_list = ["'{k}': '{v}'".format(k=k, v=v) for k, v in log_entries.items()]
    return "{ " + "; ".join(log_entries_list) + " }"