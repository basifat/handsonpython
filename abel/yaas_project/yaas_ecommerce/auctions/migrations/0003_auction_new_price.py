# Generated by Django 3.1.1 on 2020-11-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='new_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
