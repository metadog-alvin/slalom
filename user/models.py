from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class User(models.Model):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'account'
    EMAIL_FIELD = 'email'

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    account = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=60)
    team_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    role = models.IntegerField(null=True)
    last_login = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    remember_token = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'users'


# 參考
# https://www.796t.com/content/1544530152.html