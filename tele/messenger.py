from django.http import HttpResponse
from io import BytesIO
import requests
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

class Messenger():

    TELEGRAM_REQUEST_URL = "https://api.telegram.org/bot{token}/{method}"
    TELEGRAM_GET_URL = TELEGRAM_REQUEST_URL + "?chat_id={chat_id}&text={text}&parse_mode={parse_mode}"
    
    def __init__(self, token):
        self.token = token

    def send_chat(self, chat_id, text, **kwargs):
        parse_mode = kwargs.get('parse_mode', 'Markdown')
        return requests.get(self.TELEGRAM_GET_URL.format(
                method="sendMessage",
                token=self.token,
                chat_id=chat_id,
                text=text,
                parse_mode=parse_mode,
            ))

    def send_qr(self, chat_id, qr, caption=""):
        byte_io = BytesIO()
        qr.save(byte_io, 'png')
        byte_io.seek(0)

        return requests.post(self.TELEGRAM_REQUEST_URL.format(token=self.token, method='sendPhoto'), 
                data={
                    'chat_id': chat_id,
                    'caption': caption,
                },
                files={
                    'photo': (
                        'qr.png',
                        byte_io,
                        'image/png'
                    )
                }
            )