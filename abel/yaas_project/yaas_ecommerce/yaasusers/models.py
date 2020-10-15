from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import (
    BaseUserManager,AbstractBaseUser
)
from yaasusers.manager import YaasUserManager

# Create your models here.
class YaasUser(AbstractBaseUser,PermissionsMixin):
    #user=models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=255, unique=True)
    first_name= models.CharField(max_length=255 ,null=True)
    last_name=models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=20)
    text = models.CharField(max_length=20)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'created']
    objects=YaasUserManager()