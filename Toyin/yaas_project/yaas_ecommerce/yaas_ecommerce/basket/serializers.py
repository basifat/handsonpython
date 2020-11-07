from rest_framework import serializers
from basket.models import Item


class ItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = Item
        fields = '__all__'
        


#item.name, item.price, item.quantity
#item = {"name": '10', "price": '20', "quantity": 25}
#item