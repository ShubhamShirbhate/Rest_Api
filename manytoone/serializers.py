from rest_framework import serializers
from .models import Carspace, Carplan

class CarspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carspace
        fields = ('id', 'car_plan', 'car_name', 'car_model', 'production_yr')

        depth = 1