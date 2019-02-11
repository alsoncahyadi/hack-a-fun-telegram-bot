from apple import models as m
from .messenger import Messenger
from . import helpers as h
import qrcode
# from hashlib import md5

class Replier():

    def __init__ (self, token):
        self.token = token
        self.messenger = Messenger(token)

    def default(self, chat_id, message):
        return self.messenger.send_chat(chat_id, "Commandmu tidak dikenali :(\Tekan /help untuk mengetahui semua command yang ada")

    def start(self, chat_id, message):
        welcome_chat = \
"""Selamat! Kamu telah terdaftar untuk bermain di Hackafun! :D
Gunakan QR Code ini untuk mendapatkan point-mu ya!

Tekan /help untuk melihat semua command yang ada"""

        already_registered_chat = \
"""Kamu sebelumnya sudah pernah daftar!
Gunakan QR Code ini untuk mendapatkan point-mu ya!

Tekan /help untuk melihat semua command yang ada"""

        try:
            checked_player = m.Player.objects.get(id=chat_id)
        except m.Player.DoesNotExist:
            checked_player = None
            
        if checked_player:
            chat = already_registered_chat
            salt = checked_player.salt
        else:
            chat = welcome_chat
            salt = h.generate_salt()
            username = message['from'].get('username', '')
            first_name = message['from'].get('first_name', '')
            last_name = message['from'].get('last_name', '')

            new_player = m.Player(
                id = chat_id,
                salt = salt,
                username = username,
            )
            new_player.save()

        key = self._get_key(salt, chat_id, username)
        # key = md5(key.encode())
        qr = qrcode.make(key)
        return self.messenger.send_qr(chat_id, qr, chat)

    def getqr(self, chat_id, message):
        try:
            player = m.Player.objects.get(id=chat_id)
            salt = player.salt
            username = message['from'].get('username', '')
            key = self._get_key(salt, chat_id, username)
            qr = qrcode.make(key)
            return self.messenger.send_qr(chat_id, qr)
        except:
            return self.start(chat_id, message)

    def detail(self, chat_id, message):
        player = m.Player.objects.get(id=chat_id)
        detail_chat = \
"""
<code>       Game Fisik  </code><b>{physical_game_point}</b>
<code> CTR (Tournament)  </code><b>{ctr_tournament_point}</b>
<code>  CTR (Free Play)  </code><b>{ctr_free_play_point}</b>
<code>    Cerdas Cermat  </code><b>{cerdas_cermat_point}</b>
<code>        Ranking 1  </code><b>{ranking_1_point}</b>
<code>      Guitar Hero  </code><b>{guitar_hero_point}</b>
<code>            CS:GO  </code><b>{cs_go_point}</b>
<code>   Winning Eleven  </code><b>{winning_eleven_point}</b>
""".format(
        physical_game_point= player.physical_game_point,
        ctr_tournament_point = player.ctr_tournament_point,
        ctr_free_play_point = player.ctr_free_play_point,
        cerdas_cermat_point = player.cerdas_cermat_point,
        ranking_1_point = player.ranking_1_point,
        guitar_hero_point = player.guitar_hero_point,
        cs_go_point = player.cs_go_point,
        winning_eleven_point = player.winning_eleven_point,
    )

        return self.messenger.send_chat(chat_id, detail_chat, parse_mode='html')

    def help(self, chat_id, message):
        help_chat = \
"""Halo! Ini command-command yang tersedia ya:
/getqr  Menampilkan QR Code mu
/detail Menampilkan detail Hackafun mu
/help   Menampilkan menu help"""
        return self.messenger.send_chat(chat_id, help_chat)

    def reply(self, req_json, **kwargs):
        message = req_json['message']
        chat_id = message['chat']['id']
        
        function = self.map_reply_message(message)
        return function(chat_id, message)
    
    def map_reply_message(self, message):
        return {
            '/start': self.start,
            '/help': self.help,
            '/getqr': self.getqr,
            '/detail': self.detail,
        }.get(message['text'], self.default)

    def _get_key(self, salt, chat_id, username):
        chat_id_str = str(chat_id).zfill(18) # BigInt max digit
        return ';'.join([salt, chat_id_str, username])