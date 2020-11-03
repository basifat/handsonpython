from datetime import datetime, timedelta, timezone
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from yaasusers.models import YaasUser


def get_deadline():
    return datetime.now(timezone.utc) + timedelta(hours=72)


class Auction(models.Model):

    ##TODO:
    # add user
    # send email to user (seller) with an editable link
    # UI dialog before creating an auction

    AUCTION_LIFECYCLE_CHOICES = [
        ('active', 'Active'),
        ('banned', 'Banned'),
        ('due', 'Due'),
        ('resolved', 'Resolved')
    ]

    CURRENCIES_CHOICES = [
        ('eur', 'EUR '),
        ('usd', 'USD'),
        ('gbp', 'GBP'),
        ('ngn', 'NGN')

    ]

    #remove default user for field
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='seller') #default user
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='latest_bidder', default=5)# replace with actual object
    email = models.EmailField(null=True) # remove once we have actual user
    title = models.CharField(max_length=255)
    currency=models.CharField(max_length=3, choices= CURRENCIES_CHOICES, default='USD' )
    description = models.TextField()
    minimum_price = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    bidders = models.ManyToManyField(settings.AUTH_USER_MODEL) 
    deadline = models.DateTimeField(default=get_deadline)
    status= models.CharField(
        max_length=8,
        choices= AUCTION_LIFECYCLE_CHOICES,
        default= 'active'
    )


def send_updated_email(instance):
    send_mail(
        f'A new bid has been placed on {instance.title}',
        f"Someone has placed a bid of {instance.price} on {instance.title}",
        'admin@yaasacution.com',
        [instance.seller.email, instance.latest_bidder.email],
        fail_silently=False,
    )

def send_banned_email(instance):
    bidders_email = instance.bidders.values_list('email', flat=True)
    send_mail(
        f'Your auction {instance.title} has been banned',
        f"You violated our policy",
        'admin@yaasacution.com',
        [instance.seller.email, *bidders_email],
        fail_silently=False,
    )
#read up on celery
#auction -> laptop -> seller -> latest_bidder 
#auction -> pencil

#user1 -> laptop
#user1 -> pencil
#user2 -> laptop
#user3 -> laptop


#laptop -> give all users that used it before 
#user1 -> laptop
#user2 -> laptop
#user3 -> laptop
#laptop -> user1


#laptop -> many users
#user -> laptops

     


# @receiver(post_save, sender=Auction)
# def send_auction_email(sender, instance, created, **kwargs):
#     send_banned_email(instance)
#     # if created:
#     #   send_created_mail()
#     # send_updated_email()
    # pass
    


#title          #description               #minimum_price     #deadline     #status   #email   #seller
#new auction    #this is a new auction     #10                2020-10-19    #active
#new auction    #this is a new auction     #10                2020-10-19    #active
#new auction    #this is a new auction     #10                2020-10-19    #active
#new auction    #this is a new auction     #10                2020-10-19    #active
#new auction    #this is a new auction     #10                2020-10-19    #active
#new auction    #this is a new auction     #10                2020-10-19    #active
#new auction    #this is a new auction     #10                2020-10-19    #active
#new auction    #this is a new auction     #10                2020-10-19    #active



# The title of the auction.
# • The description of the item(s) to sale.
# • The minimum price. Other users should bid an amount higher than
# the minimum price.
# • The deadline: the end date and time for the auction. The minimum
# duration of an auction is 72 hours from the moment it is created. The
# expected format for the date should be clearly specied in
# the above deadline input eld.



###

# If a user bids at an auction within

# five minutes of the auction deadline, 
# the auction deadline is extended au-tomatically for an additional fiveve minutes. This allows other users to place
# new bids.

