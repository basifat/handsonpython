from django.db import models
from datetime import datetime, timedelta, timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from yaasusers.models import YaasUser
#default_user = YaasUser().objects.first()

def get_deadline():
    return datetime.now(timezone.utc) + timedelta(seconds=10)

    

class Auction(models.Model):
    
    ##TODO:
    # Add user(seller)
    # send email to user with an editable link
    # Ui dialog before creating auction.
    AUCTION_LIFECYCLE_CHOICES = [
        ("active", "Active"),
        ("banned", "Banned"),
        ("due", "Due"),
        ("resolved", "Resolved")
        
    ]
    
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='latest_bidder', default=1)
    bidders=models.ManyToManyField(settings.AUTH_USER_MODEL)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='seller')
    title = models.CharField(max_length=255)
    description=models.TextField()
    minimum_price = models.DecimalField(max_digits=7, decimal_places=2,default=1)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    deadline= models.DateTimeField(default=get_deadline)
    created_date= models.DateTimeField(auto_now_add=True)
    latest_bid_date_time= models.DateTimeField(auto_now=True)
    seller_total_bids =models.IntegerField(default=0)
    status = models.CharField(
        max_length=8,
        choices=AUCTION_LIFECYCLE_CHOICES,
        default='active'
    )








