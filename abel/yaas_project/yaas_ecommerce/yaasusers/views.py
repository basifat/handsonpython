from django.shortcuts import render
from rest_framework import viewsets
from yaasusers.models import YaasUser
from yaasusers.serializers import YaasUserSerializer

class YaasUserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = YaasUser.objects.all()
    serializer_class = YaasUserSerializer
