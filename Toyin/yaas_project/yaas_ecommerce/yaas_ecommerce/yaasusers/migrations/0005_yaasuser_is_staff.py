# Generated by Django 3.1.1 on 2020-10-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaasusers', '0004_auto_20201013_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='yaasuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]