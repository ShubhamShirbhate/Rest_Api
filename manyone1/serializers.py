from rest_framework import serializers
from .models import CarPlan, CarSpacs

class CarSpacsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpacs
        fields = ('id', 'car_plan', 'car_brand', 'car_model', 'product_yr', 'car_body', 'engine_type')
        depth = 1