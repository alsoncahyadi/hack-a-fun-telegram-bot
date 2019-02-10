import random

def generate_salt(n=5):
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars=[]
    for i in range(n):
        chars.append(random.choice(ALPHABET))

    
    return "".join(chars)

def escape_if_not_authorized(req_json):
    if req_json['message']['from']['is_bot']:
        return "Sneaky You, Bot!"