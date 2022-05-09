from time import timezone
from django.db import models

from player.models import Player as PlayerModel


# class Player:
#     player = models.OneToOneField(
#         PlayerModel,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#
#     def __str__(self):
#         return "%s the player" % self.player.name


class Enroll(models.Model):
    competition_id = models.IntegerField()
    schedule_id = models.IntegerField(null=True)
    user_id = models.IntegerField()
    player = models.ForeignKey(PlayerModel, on_delete=models.CASCADE)
    number = models.SmallIntegerField(null=True)
    order = models.SmallIntegerField(null=True)
    city = models.CharField(max_length=10, null=True)
    agency = models.CharField(max_length=50, null=True)
    level = models.CharField(max_length=50, null=True)
    group = models.CharField(max_length=50, null=True)
    item = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=1, null=True)
    coach = models.CharField(max_length=30, null=True)
    leader = models.CharField(max_length=30, null=True)
    manager = models.CharField(max_length=30, null=True)
    director = models.CharField(max_length=30, null=True)
    sound = models.CharField(max_length=100, null=True)
    check_in_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # player_name = models.OneToOneField(PlayerModel, on_delete=models.CASCADE)

    # player_name = models.ForeignKey(PlayerModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'enrolls'
