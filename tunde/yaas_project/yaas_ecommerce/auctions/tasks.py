from celery.decorators import task
from celery.schedules import crontab
from auctions.models import Auction
from django.core.mail import send_mail



@task(name="sum_two_numbers")
def add(x, y):
    print(x + y, "printed sum")
    return x + y


@task(name="scheduled_send_winning_bidder_email")
def scheduled_send_winning_bidder_email():
    due_auctions = Auction.objects.filter(status='due')


    for auction in due_auctions:
        bidders_email = auction.bidders.values_list('email', flat=True)
        send_mail(
        f'Auction {auction.title} has been won by {auction.bidder}',
        f"We have an Auction Winner",
        'admin@yaasacution.com',
        [auction.seller.email, *bidders_email],
        fail_silently=False,
        )
        auction.status='resolved' #assignment should use value defined in class directly.
        auction.save()


#1. Auction.objects.filter(status='due') ##djdjdjdjdjdjdjdjd
#2. Auction.objects.filter(status='due') []










# @periodic_task(run_every=(crontab(minute='*/15')), name="periodicly_sum_two_numbers", ignore_result=True)
# def periodic_add(x, y):
#     return x + y


