# Generated by Django 3.1.1 on 2020-10-06 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yaasusers', '0002_yaasuser_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yaasuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='yaasuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='yaasuser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='yaasuser',
            name='user_permissions',
        ),
    ]