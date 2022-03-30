from rest_framework import serializers
from .models import NbaNews
from django.contrib.auth import get_user_model

User = get_user_model()

class NbaNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = NbaNews
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
