# Generated by Django 3.1.1 on 2020-10-13 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auctions', '0005_auction_latest_bidder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='seller',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='yaasusers.yaasuser'),
        ),
    ]