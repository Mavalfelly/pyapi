from .models import Cars
from rest_framework import serializers

class CarSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Cars
        fields='__all__'