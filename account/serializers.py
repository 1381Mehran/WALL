from rest_framework import serializers
from .models import UserAccount
from ads.serializers import AdSerializer


class UserAccountSerializer(serializers.ModelSerializer):
    publisher_ads = AdSerializer(many=True)
    class Meta:
        model = UserAccount
        fields = ('username', 'publisher_ads')
