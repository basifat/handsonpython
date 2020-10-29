from datetime import datetime, timedelta, timezone
import pytz

from rest_framework import serializers

from auctions.models import Auction
from auctions.tasks import task_send_created_email

class AuctionSerializer(serializers.ModelSerializer):

    class Meta:
        model= Auction
        fields = '__all__'
        read_only_fields = ['bidder','seller','deadline','latest_bid_date_time' ,'seller_total_bids','bidders']

    def get_user(self):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
           user = request.user
        return user
    
    
    def create(self, validated_data):
        user=self.get_user()
        validated_data['seller']= user
        instance= super().create(validated_data)
        task_send_created_email.delay(instance.id)
        return instance
        # return super().create(validated_data)
    
    def update(self, instance, validated_data):
        bid_time = datetime.now(timezone.utc)
        minutes_apart = instance.deadline - bid_time
        if (minutes_apart.seconds % 3600 / 60.0) <= 20:
            instance.deadline = instance.deadline + timedelta(minutes=5)
        #instance.latest_bidder=validated_data['seller']
        instance.seller_total_bids=instance.seller_total_bids + 1
        user=self.get_user()
        instance.bidder= user
        instance.bidders.add(user)
        instance.bidders.values_list()
        
        return super().update(instance, validated_data)