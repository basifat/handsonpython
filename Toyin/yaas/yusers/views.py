from rest_framework import viewsets, views
from rest_framework.response import Response
from django.http import HttpResponse

from yusers.models import Dancing
from yusers.serializers import DancingSerializer

class DancingViewSet(viewsets.ModelViewSet):
    queryset = Dancing.objects.all()
    serializer_class = DancingSerializer

def debby(request):
    info = Dancing.objects.all()
    return HttpResponse(info)



class DancingCreateView(views.APIView):

    serializer_class = DancingSerializer

    def post(self, request):
        name = request.data["name"]
        email = request.data["email"]
        # lang_instance = YaasUserLanguage.objects.get(id=language)

        user = Dancing.objects.create(username=username,email=email)

        return HttpResponse(user)