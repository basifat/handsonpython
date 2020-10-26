from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
from yaasusers.manager import YaasUserManager

class YaasUser(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=20, unique=True)
  first_name= models.CharField(max_length=255,null=True)
  last_name= models.CharField(max_length=255,null=True)
  email = models.CharField(max_length=20)
  created = models.DateTimeField(auto_now_add=True)
  is_staff= models.BooleanField(default=False)
  

  REQUIRED_FIELDS = ['email', 'created']
  USERNAME_FIELD = 'username'
  objects=YaasUserManager()



#Add a new model called YaasUserLanguage
#language = "english"
#lang_iso = "GB-en"
#user = YaasUser (as a foreign key)

#make an API example /languages/4
#language: english
#lang_iso: GB-en
#user select

#Model
#Views
#Serializers
#Endpoint
