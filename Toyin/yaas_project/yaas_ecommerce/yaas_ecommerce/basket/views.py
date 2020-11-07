from rest_framework import viewsets
from rest_framework.response import Response

from basket.models import Item
from basket.serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = ItemSerializer
    queryset = Item.objects.all()




def tundefn(request):
    return HttpResponse(items)

def homepage(request):
    items = Item.objects.all()
    template = loader.get_template('basket/index.html')
    context = {
        'item_selected_list': items,
    }
    return HttpResponse(template.render(context, request))


#model (database table) -> view -> url -> respose
#model (database table) -> serializer -> view (viewset) -> urls(routers) -> response
# curl endpoint vs public apps



  