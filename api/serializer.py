from rest_framework import serializers
from .models import Emp


class WeatherSerializer(serializers.Serializer):

    Zip     = serializers.CharField(max_length = 10)
    city    = serializers.CharField(max_length = 10)
    phone   = serializers.IntegerField()

    def __str__(self):
        return "Serializer Objects"    



class EmpSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Emp
        fields  = ('__all__')

