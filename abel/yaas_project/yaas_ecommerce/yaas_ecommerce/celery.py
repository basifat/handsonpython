from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yaas_ecommerce.settings')
app = Celery('yaas_ecommerce')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#celery -A yaas_ecommerce beat -l info

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    # 'run-when-auction-created': {
    #     'task': 'task_send_created_email',
    #     'schedule': crontab(day_of_week='mon',minute='*/25'),
    #     'args': ()
    # },
    'run-every-one-seconds': {
        'task': 'scheduled_send_winning_bidder_email',
        'schedule': crontab(day_of_week='mon',minute='*/1'),
        'args': ()
    },
}