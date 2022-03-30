"""
WSGI config for django_practice_01 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_practice_01.settings')
django.setup()
from apscheduler.schedulers.background import BackgroundScheduler
from nbanews.beautifulsoup import collectNews

application = get_wsgi_application()

print('uwsgi')
scheduler = BackgroundScheduler(timezone='Asia/Taipei')
scheduler.add_job(collectNews,
                  'interval',
                  seconds=10,
                  id='collectNews',
                  replace_existing=True)
scheduler.start()
print('scheduler started')
