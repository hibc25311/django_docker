from django.urls import path
from nbanews import views

urlpatterns = [
    path('nbanews', views.nbanews, name='nbanews'),
    path('', views.index, name='index')
]