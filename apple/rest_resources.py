from django.contrib.auth.models import User
from rest_framework import viewsets, serializers as s
from django.conf import settings
from django.forms import model_to_dict
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.fields import SerializerMethodField
from datetime import datetime
from .models import *

# Serializer
class PlayerSerializer(s.ModelSerializer):
  class Meta:
    model = Player
    fields = (
      'username',
      'ctr_tournament_point',
      'ctr_free_play_point',
      'cerdas_cermat_point',
      'ranking_1_point',
      'guitar_hero_point',
      'cs_go_point',
      'winning_eleven_point',
      'baby_rattle_point',
      'move_up_cup_point',
      'jumping_the_riddles_point',
      'inferno_extinguisher_point',
      'floating_ball_race_point',
      'human_table_soccer_point',
    )


class TransactionSerializer(s.ModelSerializer):
  class Meta:
    model = Transaction
    fields = '__all__'

# ViewSet
class PlayerViewSet(viewsets.ModelViewSet):
  queryset = Player.objects.all()
  serializer_class = PlayerSerializer


class TransactionViewSet(viewsets.ModelViewSet):
  queryset = Transaction.objects.all()
  serializer_class = TransactionSerializer
