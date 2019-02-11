from django.db import models as m
from django.contrib.auth import get_user_model

# Create your models here.
# Revenue
class Player(m.Model):
    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"
  
    def __str__(self):
        return "{} | ID: {}".format(self.__class__.__name__, self.id)

    id = m.BigIntegerField(verbose_name="Player ID", primary_key=True)
    username = m.CharField(verbose_name="Username", max_length=32, default='', db_index=True)
    first_name = m.CharField(verbose_name="First Name", max_length=32, default='')
    last_name = m.CharField(verbose_name="Last Name", max_length=32, default='')
    salt = m.CharField(verbose_name="Player's salt", max_length=16)
    physical_game_point = m.IntegerField(verbose_name = "Physical Game Point", default=0)
    ctr_tournament_point = m.IntegerField(verbose_name = "CTR (Tournament) Point", default=0)
    ctr_free_play_point = m.IntegerField(verbose_name = "CTR (Free Play) Point", default=0)
    cerdas_cermat_point = m.IntegerField(verbose_name = "Cerdas Cermat Point", default=0)
    ranking_1_point = m.IntegerField(verbose_name = "Ranking 1 Point", default=0)
    guitar_hero_point = m.IntegerField(verbose_name = "Guitar Hero Point", default=0)
    cs_go_point = m.IntegerField(verbose_name = "CS:GO Point", default=0)
    winning_eleven_point = m.IntegerField(verbose_name = "Winning Eleven Point", default=0)


class Transaction(m.Model):
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
  
    def __str__(self):
        return "{} | ID: {}".format(self.__class__.__name__, self.id)

    id = m.AutoField(verbose_name="Player ID", primary_key=True)
    player = m.ForeignKey(Player, verbose_name="Player", on_delete=m.DO_NOTHING, db_index=True)
    staff = m.ForeignKey(get_user_model(), verbose_name="Staff", on_delete=m.DO_NOTHING)
    point = m.IntegerField(verbose_name = "Point")
    game_type = m.SmallIntegerField(verbose_name = "game_type")
    