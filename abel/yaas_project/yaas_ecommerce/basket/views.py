from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.response import Response
from basket.models import Item
from basket.serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = Item.objects.filter(id=5)
    serializer_class = ItemSerializer

def tunde(request):
    items=Item.objects.all()
    return HttpResponse(items)

def homepage(request):
    items= Item.objects.all()
    template = loader.get_template('basket/index.html')
    context = {
        'item_selected_list': items,
    }
    return HttpResponse(template.render(context, request))
    





    



