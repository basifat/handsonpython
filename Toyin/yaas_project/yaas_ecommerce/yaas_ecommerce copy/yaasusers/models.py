from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
from yaasusers.manager import YaasUserManager



# Assignment 

# Add views,serializer and endpoint for YaasUserLanguage
# create a YaasUserLanguage using the endpoint i.e /languages
# take the id of the language create and use it as the default language for YaasUserLanguage


#python manage.py shell
#from yaasusers.models import YaasUserLanguage
#YaasUserLanguage.objects.create(...)


#Run migrations for YaasUser and also create a new YaasUser 
# that would use the one of the two languages already created as its language


#######
#Create a new Template view that uses a template called 'auctions.html'
# Add a text in english and also add a gibberish text in another language i.e FI
# Allow Django to pick the language that corresponds to the one the user has on their profile





class YaasUserLanguage(models.Model):

  language =models.CharField(max_length=40, null=True)
  lang_iso= models.CharField(max_length=40, null=True)
  country=models.CharField(max_length=40, null=True)

  def __str__(self):
    return self.language

class YaasUser(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=20, unique=True)
  first_name= models.CharField(max_length=255,null=True)
  last_name= models.CharField(max_length=255,null=True)
  email = models.CharField(max_length=20)
  created = models.DateTimeField(auto_now_add=True)
  is_staff= models.BooleanField(default=False)
  language= models.ForeignKey(YaasUserLanguage, on_delete=models.CASCADE, default=1)
  

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
