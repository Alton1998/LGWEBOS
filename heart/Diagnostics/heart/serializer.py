from rest_framework import serializers
from . models import Heart

class HeartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Heart
        fields=('__all__')

