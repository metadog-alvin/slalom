from django.db import models


class User(models.Model):
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=60)
    team_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    role = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    remember_token = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'users'
