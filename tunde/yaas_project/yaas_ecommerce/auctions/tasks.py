from datetime import datetime, timezone
from celery.decorators import task
from celery.schedules import crontab
from auctions.models import Auction
from django.core.mail import send_mail


def is_past_deadline(instance):
    current_time=datetime.now(timezone.utc)
    return current_time > instance.deadline

@task(name="task_send_created_email")
def task_send_created_email(created_id):
    instance=Auction.objects.get(id=created_id)

    send_mail(
        f'New Auction {created_id} Created',
        f"You've just created a new auction with title {instance.title}",
        'admin@yaasacution.com',
        [instance.seller.email],
        fail_silently=False,
    )        

@task(name="scheduled_send_winning_bidder_email")
def scheduled_send_winning_bidder_email():
    for auction in Auction.objects.filter(status='active'):
        if is_past_deadline(auction):
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


