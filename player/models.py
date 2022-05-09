from django.db import models


class Player(models.Model):
    identity = models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=1, null=True)
    city = models.CharField(max_length=10, null=True)
    agency = models.CharField(max_length=50, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'players'