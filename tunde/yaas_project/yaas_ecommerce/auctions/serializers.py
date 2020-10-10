from datetime import datetime, timedelta, timezone
import pytz

from rest_framework import serializers

from auctions.models import Auction


class AuctionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Auction
        fields = '__all__'
        read_only_fields = ['latest_bidder', 'deadline']


    def update(self, instance, validated_data):
        bid_time = datetime.now(timezone.utc)
        minutes_apart = instance.deadline - bid_time
        if (minutes_apart.seconds % 3600 / 60.0) <= 20:
            instance.deadline = instance.deadline + timedelta(minutes=5)
        instance.latest_bidder = validated_data['seller']
        return super().update(instance, validated_data)

        
