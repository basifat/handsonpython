from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rest_framework.response import Response
from django.conf import settings
from django.utils.translation import gettext, activate, get_language
from django.utils.translation import gettext as _
from rest_framework import viewsets, views
from rest_framework.generics import ListAPIView
from yaasusers.models import YaasUser, YaasUserLanguage
from yaasusers.serializers import YaasUserSerializer, YaasUserLanguageSerializer
from rest_framework.renderers import JSONRenderer


class YaasUserCreateView(views.APIView):

    serializer_class = YaasUserSerializer

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        email = request.data["email"]
        language = request.data["language"]
        print(username, "username")

        lang_instance = YaasUserLanguage.objects.get(id=language)

        user = YaasUser.objects.create(username=username, password=password, language=lang_instance, email=email)

        return HttpResponse(user)


class YaasUserListView(views.APIView):

    serializer_class = YaasUserSerializer

    def get_queryset(self):
        return YaasUser.objects.all() ## sellers in uk

    def get(self, request):

        return Response(self.get_serializer(self.get_queryset(), many=True).data)




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
        'language_list': [
        _("Welcome to django webshop"), 
        _("Random to django webshop")],
    }

    response =  HttpResponse(template.render(context, request))
    # response.set_cookie(settings.LANGUAGE_COOKIE_NAME, "sv")
    return response



def translate_text(request):
    # activate('sv')
    # print(get_language(), "get_language")
    # request.LANGUAGE_CODE = 'sv'
    # print(request.LANGUAGE_CODE, " request.LANGUAGE_CODE")
    output = _("Welcome to django webshop")
    return HttpResponse(output)


# #sv.po
# msgid "Ambiguous translatable block of text"
# msgstr "Valkommen blah blah"


# #fi.po
# msgid "Ambiguous translatable block of text"
# msgstr "Terve tuloa blah blah"

# msgid "Welcome and click here"
# msgstr "Terve tuloa klicka"





