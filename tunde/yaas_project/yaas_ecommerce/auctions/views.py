from django.shortcuts import render
from rest_framework import viewsets
from auctions.models import Auction
from auctions.serializers import AuctionSerializer
from rest_framework.exceptions import APIException
from django.http import HttpResponse
from rest_framework.response import Response
from datetime import datetime, timedelta, timezone
import pytz

class SameSellerException(APIException):
    status_code = 500
    default_detail = 'Seller cannot bid on own auction'
    default_code = 'seller_cannot_bid'

class WinningBidderException(APIException):
    status_code = 500
    default_detail = 'You cannot bid on an auction you"re already winning'
    default_code = 'winning_bidder_cannot_bid'


class BidTooLowException(APIException):
    status_code = 500
    default_detail = 'Current bid must be greater than previous bid'
    default_code = 'seller_cannot_bid_lesseer_amount'


class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    filterset_fields = ['title']

    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = self.get_object()
  
            if float(request.data["price"]) < instance.price:
                raise BidTooLowException

            if instance.seller == request.data["seller"]:
                raise SameSellerException
            
            if instance.latest_bidder == request.data["seller"]:
                raise WinningBidderException
        
        return super().update(request, *args, **kwargs)

# If a user bids at an auction within five minutes of the auction deadline, 
# the auction deadline is extended au-tomatically for an additional fiveve minutes. This allows other users to place
# new bids.


# If a user bids at an auction within five minutes of the auction deadline,


#2.get the time of the bid
#3.check if it's within 5min of the auction deadline 


# the auction deadline is extended au-tomatically for an additional fiveve minutes. This allows other users to place
# new bids.

# deadline + 5min



#CRUD
#CREATE, UPDATE, RETRIEVE



# class AuctionBid:

#auctions/10
# price =  10.00
# price =  price + bid_price
#1. Auction
#2. prie information
#The minimum bid increment is 0.01. Only two decimal places are considered when bidding.
# A seller cannot bid on own auctions.


#Assignment1
#Add a new field to auction called latest_bid_date_time 
#Update the latest_bid_date_time everytime someone bids on an auction 
#Make the field read only so that it is not available on the API form.

#Assignment2
#Add a new field to auction called seller_total_bids 
# Know the seller(bidder) that is bidding 
# Add 1 to the sellers total bid count
#Make the field read only so that it is not available on the API form.










