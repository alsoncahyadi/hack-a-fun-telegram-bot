from rest_auth.registration.views import LoginView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser, FormParser
from rest_framework import permissions
from django.db import transaction
from .rest_resources import PlayerSerializer
from .models import *
import tele.helpers as h
import json
import os

class AddPoint(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser, FormParser)
    
    @transaction.atomic
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
                self._add_game_point(player, data['game_type'], int(data['point']))
            except:
                return h.error_response(422, "Invalid game_type: {}".format(data['game_type']))

            if os.environ.get('SAVE_TRANSACTION', 'TRUE') == 'TRUE':
                staff = request.user
                t = Transaction(player=player, staff=staff, point=data['point'], game_type = h.game_type_to_i(data['game_type']))
                t.save()
            
            return HttpResponse(json.dumps({
                    'message': PlayerSerializer(player).data,
                    'code': 201
                }),
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

    def _add_game_point(self, player, game_type, point):
        old_point = getattr(player, game_type + "_point")
        setattr(player, game_type + "_point", old_point + point)
        player.save()


class LoginViewCustom(LoginView):
    authentication_classes = (TokenAuthentication,)


def healthz(request):
    permissions.IsAuthenticated()
    return HttpResponse("OK")