from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.


class UserProfile(AbstractUser):
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username

    @property
    def token(self):
        refresh = RefreshToken.for_user(self)
        return str(refresh.access_token)


