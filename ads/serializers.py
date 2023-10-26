from rest_framework import serializers
from .models import Ad


class AdSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Ad
        exclude = ['is_public']
        read_only_fields = ('id', 'publisher', 'is_public', 'date_added')
        extra_kwargs = {'image': {'required': False},
                        'caption': {'required': False}}

