from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from datetime import datetime
from auctions.models import Auction
from decimal import Decimal
import requests
from auctions.serializers import AuctionSerializer
from auctions.tasks import task_send_new_bid_email, task_send_banned_email



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

class BannedAuctionException(APIException):
    status_code = 500
    default_detail = 'You cannot bid on a banned'
    default_code = 'can not bid banned auction'


    
class AuctionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    #queryset = Auction.objects.exclude(status='banned')
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    filterset_fields=['title']
    

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    currencies = {'eur': 1, 'gbp': 1.11, 'ngn': 500.00} 
    
   

       
            

   
    def update(self, request, *args, **kwargs):
        print(request.user)
        if request.method == "PUT":
            instance = self.get_object()
  
            if float(request.data["price"]) <=instance.price:
                raise BidTooLowException
        
            # if instance.seller.id == int(request.user.id):
            #     raise SameSellerException
            
            # if instance.bidder.id == int(request.user.id):
            #     raise WinningBidderException
            if instance.status =='banned':
                raise BannedAuctionException
            
            response = super().update(request, *args, **kwargs)
         
            if request.data['status']=='banned':
                task_send_banned_email.delay(instance.id)
                return response
              
            task_send_new_bid_email.delay(instance.id)
            return response

    
#Assignment 1
# delacare a dictionary called currencies. It will ahve each of the currency we care about and their multiplier values
# i.e currencies = {eur: 1, gbp: 1.11, ngn: 500}
# When a user chooses gbp, we want the existing price to be multiplied by the currency multiplier.
# i.e 
# currency = gbp
# (old) price = 100 
# (new) price = 111
#task: 




