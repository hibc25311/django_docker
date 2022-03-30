from django.urls import path, re_path
from nbanews import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import NbaNewsDetail, NbaNewsList

urlpatterns = [
    path('nbanews', views.nbanews, name='nbanews'),
    path('', views.index, name='index'),
    re_path(r'^nbanews/$', views.NbaNewsList.as_view()),
    re_path(r'^nbanews/(?P<pk>[0-9]+)$', views.NbaNewsDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

#not startup when running server by uwsgi
"""
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from nbanews.beautifulsoup import collectNews


scheduler = BackgroundScheduler(timezone='Asia/Taipei')
scheduler.add_job(collectNews,
                  'interval',
                  seconds=10,
                  id='collectNews',
                  replace_existing=True)
scheduler.start()
print('scheduler started')"""
