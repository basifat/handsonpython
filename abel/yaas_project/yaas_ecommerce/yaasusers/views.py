from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.utils.translation import gettext
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


def welcome(request):

    languages = YaasUserLanguage.objects.all()
    template = loader.get_template('yaasusers/welcome.html')
    context = {
        'language_list': languages,
    }
    return HttpResponse(template.render(context, request))

def language_page(request, language_id):
    language_object=YaasUserLanguage.objects.get(id=language_id)
    return HttpResponse(language_object)

def translate_text(request):
    #{% load i18n %}
    language = YaasUserLanguage.objects.get(id=3)
    output = gettext("Welcome to django webshop")
    return HttpResponse(output, language)




