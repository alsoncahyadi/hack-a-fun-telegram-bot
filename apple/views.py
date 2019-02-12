from rest_auth.registration.views import LoginView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser, FormParser
from rest_framework import permissions
from django.db import transaction
from .rest_resources import PlayerSerializer
from .models import *
from tele.messenger import Messenger
import tele.helpers as h
import json
import os, traceback

TOKEN = os.environ['TELE_TOKEN']
messenger = Messenger(TOKEN)

class AddPoint(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser, FormParser)

    point_added_notification_message = "🙌🎊🎉 Woohoo! Point {game_name} kamu telah ditambah sebesar {point} menjadi {final_value} 🎉🎊🙌"
    
    def post(self, request):
        print(h.get_log(request))
        data = request.data
        if self._is_data_valid(data):
            # Validate chat_id
            try:
                chat_id = int(data['chat_id'])
                player = Player.objects.get(id=chat_id)
            except Player.DoesNotExist:
                return h.error_response(404, "Player not found")

            # Validate salt
            if data['salt'] != player.salt:
                return h.error_response(403, "Forbidden, wrong NaCl")

            # Validate game_type
            try:
                _, new_point, _ = self._add_game_point(player, data['game_type'], int(data['point']), request.user)
            except AttributeError:
                return h.error_response(422, "Invalid game_type: {}".format(data['game_type']))
            except:
                return h.error_response(500, "Error saving {}".format(data))

            # Notify user
            try:
                response = messenger.send_chat(chat_id, self.point_added_notification_message.format(
                    game_name = h.game_type_s_to_name(data['game_type']),
                    point = int(data['point']),
                    final_value = new_point,
                ))
                print("> INFO : Notif status {} for {}".format(response, data['chat_id']))
            except:
                print("> ERROR: Failed sending notif to {} with trace {}".format(data['chat_id'], traceback.format_exc(5).splitlines(),))

            # Return response
            return JsonResponse({
                    'message': PlayerSerializer(player).data,
                    'code': 201
                },
                status=201,
            )
        else:
            return h.error_response(422, "Invalid key or incomplete payload")

    def _is_data_valid(self, data):
        required_params = ('game_type', 'point', 'chat_id', 'salt')
        try:
            return set(data.keys()) == set(required_params)
        except:
            return False

    def _parse_params(self, request):
        return json.loads(request.body)

    @transaction.atomic
    def _add_game_point(self, player, game_type, point, staff=None):
        old_point = getattr(player, game_type + "_point")
        new_point = old_point + point
        setattr(player, game_type + "_point", new_point)
        player.save()

        t = None
        if os.environ.get('SAVE_TRANSACTION', 'TRUE') == 'TRUE':
            t = Transaction(player=player, staff=staff, point=point, game_type = h.game_type_to_i(game_type))
            t.save()
        return old_point, new_point, t


class LoginViewCustom(LoginView):
    authentication_classes = (TokenAuthentication,)


def healthz(request):
    permissions.IsAuthenticated()
    return HttpResponse("OK")