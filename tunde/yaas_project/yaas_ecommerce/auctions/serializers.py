from datetime import datetime, timedelta, timezone
import pytz

from rest_framework import serializers

from auctions.models import Auction
from yaasusers.models import YaasUser


class AuctionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Auction
        fields = '__all__'
        read_only_fields = ['latest_bidder', 'deadline', 'bidders','seller']

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
           user = request.user

        validated_data['seller']= user
        return super().create(validated_data)
        

    def update(self, instance, validated_data):
        bid_time = datetime.now(timezone.utc)
        minutes_apart = instance.deadline - bid_time

        if (minutes_apart.seconds % 3600 / 60.0) <= 20:
            instance.deadline = instance.deadline + timedelta(minutes=5)
        #instance.latest_bidder = validated_data['seller']
     
        

        return super().update(instance, validated_data)

        
