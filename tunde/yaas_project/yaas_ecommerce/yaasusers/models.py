from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin


class YaasUser(models.Model):
  user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  username = models.CharField(max_length=20, unique=True)
  password = models.CharField(max_length=20)
  email = models.CharField(max_length=20)
  text =  models.CharField(max_length=20)
#   created = models.DateTimeField(auto_now_add=True)
#   is_anonymous =  models.BooleanField(default=False)
#   is_authenticated = models.BooleanField(default=False)

  REQUIRED_FIELDS = ['email']
  USERNAME_FIELD = 'username'
