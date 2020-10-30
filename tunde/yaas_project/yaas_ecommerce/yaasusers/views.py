from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rest_framework import viewsets
from yaasusers.models import YaasUser, YaasUserLanguage
from yaasusers.serializers import YaasUserSerializer, YaasUserLanguageSerializer


class YaasUserViewSet(viewsets.ModelViewSet):
    queryset = YaasUser.objects.all()
    serializer_class = YaasUserSerializer

class YaasUserLanguageViewSet(viewsets.ModelViewSet):
    queryset = YaasUserLanguage.objects.all()
    serializer_class = YaasUserLanguageSerializer


def language_page(request, language_id):
    _("Ambiguous translatable block of text")
    language_object=YaasUserLanguage.objects.get(id=language_id)
    return HttpResponse(language_object)

def welcome(request):

    languages = YaasUserLanguage.objects.all()
    template = loader.get_template('yaasusers/welcome.html')
    context = {
        'language_list': languages,
    }
    return HttpResponse(template.render(context, request))



# #sv.po
# msgid "Ambiguous translatable block of text"
# msgstr "Valkommen blah blah"


# #fi.po
# msgid "Ambiguous translatable block of text"
# msgstr "Terve tuloa blah blah"

# msgid "Welcome and click here"
# msgstr "Terve tuloa klicka"





