from django.shortcuts import render
from nbanews.models import NbaNews
from django.http import HttpResponse, Http404

from rest_framework import generics
from rest_framework.views import APIView
from .serializers import NbaNewsSerializer
# Create your views here.


def index(request):
    return HttpResponse("I am Django 3.1 !!!")


def nbanews(request):
    last_ten_news = NbaNews.objects.all().order_by('-id')[:10]

    return render(request, 'nbanews/nbanews.html',
                  {'last_ten_news': last_ten_news})


# generic class-based views
class NbaNewsList(generics.ListCreateAPIView):
    queryset = NbaNews.objects.all()
    serializer_class = NbaNewsSerializer

    def perform_create(self, serializer):
        serializer.save()


class NbaNewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NbaNews.objects.all()
    serializer_class = NbaNewsSerializer
