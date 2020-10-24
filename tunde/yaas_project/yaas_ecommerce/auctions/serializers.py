from datetime import datetime, timedelta, timezone
import pytz

from rest_framework import serializers

from auctions.models import Auction
from yaasusers.models import YaasUser
from auctions.tasks import task_send_created_email


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


        if (minutes_apart.seconds % 3600 / 60.0) <= 20:
            instance.deadline = instance.deadline + timedelta(minutes=5)
        instance.bidder = user
        print(instance.bidders.values_list('email', flat=True))
        instance.bidders.add(user)

        return super().update(instance, validated_data)

        