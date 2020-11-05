from datetime import datetime, timedelta, timezone
import pytz

from rest_framework import serializers

from auctions.models import Auction
from yaasusers.models import YaasUser
from auctions.tasks import task_send_created_email
from decimal import Decimal



def currency_converter(amount, to_currency):
    currency_converter= { 
    'eur': 0.85, 
    'gbp': 0.89,
    'ngn': 5
    }
    return amount * currency_converter[to_currency]


class AuctionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Auction
        fields = '__all__'
        read_only_fields = ['bidder', 'deadline', 'bidders','seller']

    def get_user(self):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
           user = request.user
        
        return user

    def create(self, validated_data):
        user = self.get_user()

        validated_data['seller']= user
        instance= super().create(validated_data)
        task_send_created_email.delay(instance.id)
        return instance
        

    def update(self, instance, validated_data):
        bid_time = datetime.now(timezone.utc)
        minutes_apart = instance.deadline - bid_time

        user = self.get_user()
        exchanged = currency_converter(float(instance.price), validated_data['currency'])

        if (minutes_apart.seconds % 3600 / 60.0) <= 20:
            instance.deadline = instance.deadline + timedelta(minutes=5)

        instance.bidder = user
        instance.bidders.add(user)
        
        validated_data['price'] = Decimal(round(exchanged, 2)) 


        return super().update(instance, validated_data)

        