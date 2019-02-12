from django.db import models as m
from django.contrib.auth import get_user_model
import tele.helpers as h

# Create your models here.
# Revenue
class Player(m.Model):
    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"
  
    def __str__(self):
        return "[{}]  @{}".format(
            self.id,
            self.username,
        )
        

    id = m.BigIntegerField(verbose_name="Player ID", primary_key=True)
    username = m.CharField(verbose_name="Username", max_length=32, default='', db_index=True)
    salt = m.CharField(verbose_name="Player's salt", max_length=16)
    ctr_tournament_point = m.IntegerField(verbose_name = "CTR (Tournament) Point", default=0)
    ctr_free_play_point = m.IntegerField(verbose_name = "CTR (Free Play) Point", default=0)
    cerdas_cermat_point = m.IntegerField(verbose_name = "Cerdas Cermat Point", default=0)
    ranking_1_point = m.IntegerField(verbose_name = "Ranking 1 Point", default=0)
    guitar_hero_point = m.IntegerField(verbose_name = "Guitar Hero Point", default=0)
    cs_go_point = m.IntegerField(verbose_name = "CS:GO Point", default=0)
    winning_eleven_point = m.IntegerField(verbose_name = "Winning Eleven Point", default=0)
    baby_rattle_point = m.IntegerField(verbose_name = "Baby Rattle Point", default = 0)
    move_up_cup_point = m.IntegerField(verbose_name = "Move Up Cup Point", default = 0)
    jumping_the_riddles_point = m.IntegerField(verbose_name = "Jumping the Riddles Point", default = 0)
    inferno_extinguisher_point = m.IntegerField(verbose_name = "Inferno Extinguisher Point", default = 0)
    floating_ball_race_point = m.IntegerField(verbose_name = "Floating Ball Race Point", default = 0)
    human_table_soccer_point = m.IntegerField(verbose_name = "Huma Table Soccer Point", default = 0)


class Transaction(m.Model):
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
  
    def __str__(self):
        return "{}  |  for {} by {}; {}; {}".format(self.id, self.player, self.staff, h.game_type_to_s(self.game_type), self.point)

    id = m.AutoField(verbose_name="Player ID", primary_key=True)
    player = m.ForeignKey(Player, verbose_name="Player", on_delete=m.SET_NULL, db_index=True, null=True)
    staff = m.ForeignKey(get_user_model(), verbose_name="Staff", on_delete=m.SET_NULL, null=True)
    point = m.IntegerField(verbose_name = "Point")
    game_type = m.SmallIntegerField(verbose_name = "game_type")
    