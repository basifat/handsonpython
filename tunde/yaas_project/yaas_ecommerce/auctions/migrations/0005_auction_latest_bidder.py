# Generated by Django 3.1.1 on 2020-10-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auction_minimum_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='latest_bidder',
            field=models.CharField(max_length=20, null=True),
        ),
    ]