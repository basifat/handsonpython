from django.shortcuts import render
from rest_framework import viewsets
from yaasusers.models import YaasUser, YaasUserLanguage
from yaasusers.serializers import YaasUserSerializer, YaasUserLanguageSerializer

class YaasUserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = YaasUser.objects.all()
    serializer_class = YaasUserSerializer


class YaasUserLanguageViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = YaasUserLanguage.objects.all()
    serializer_class =YaasUserLanguageSerializer
