import random

def generate_salt():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars=[]
    for i in range(16):
        chars.append(random.choice(ALPHABET))

    
    return "".join(chars)

def send_message(chat_id, text):
    return HttpResponse(
        requests.get(TELEGRAM_GET_URL.format(
            method="sendMessage",
            token=TOKEN,
            chat_id=chat_id,
            text=text
        )).content
    )