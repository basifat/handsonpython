from datetime import datetime, timedelta, timezone
import pytz

from rest_framework import serializers

from auctions.models import Auction

class AuctionSerializer(serializers.ModelSerializer):

    class Meta:
        model= Auction
        fields = '__all__'
        read_only_fields = ['latest_bidder', 'deadline','latest_bid_date_time' ,'seller_total_bids']

    
    def update(self, instance, validated_data):
        bid_time = datetime.now(timezone.utc)
        minutes_apart = instance.deadline - bid_time
        if (minutes_apart.seconds % 3600 / 60.0) <= 20:
            instance.deadline = instance.deadline + timedelta(minutes=5)
        instance.latest_bidder = validated_data['seller']
        if validated_data['price'] > instance.price:
            instance.seller_total_bids=instance.seller_total_bids + 1
        
        return super().update(instance, validated_data)