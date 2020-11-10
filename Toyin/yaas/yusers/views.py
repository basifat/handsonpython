from rest_framework import viewsets, views
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView

from yusers.models import Dancing
from yusers.serializers import DancingSerializer

class DancingViewSet(viewsets.ModelViewSet):
    queryset = Dancing.objects.all()
    serializer_class = DancingSerializer

def debby(request):
    info = Dancing.objects.all()
    return HttpResponse(info)



# class DancingCreateView(views.APIView):

#     serializer_class = DancingSerializer

#     def post(self, request):
#         name = request.data["name"]
#         email = request.data["email"]
#         # lang_instance = YaasUserLanguage.objects.get(id=language)

#         user = Dancing.objects.create(username=username,email=email)

#         return HttpResponse(user)


class DancingView(APIView):

    def get(self, request):
        dancing = Dancing.objects.all()
        return Response({"dancing": dancing})  


    def post(self, request):
        user = Dancing.objects.create(
                name=request.data.get('name'),
                email=request.data.get('email'),
            )
        user.set_name(str(request.data.get('name')))
        user.save()
        return Response({"status":"success","response":"Successfully Created"})
          