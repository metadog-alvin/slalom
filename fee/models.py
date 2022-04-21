from django.db import models


class Fee(models.Model):
    user_id = models.IntegerField()
    player_id = models.IntegerField()
    competition_id = models.IntegerField()
    fee = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'fee'
