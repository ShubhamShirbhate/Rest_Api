from django.shortcuts import render
from rest_framework import viewsets
from .models import CarSpacs, CarPlan
from .serializers import CarSpacsSerializer
from rest_framework.response import Response

class CarView(viewsets.ModelViewSet):
    queryset = CarSpacs.objects.all()
    serializer_class = CarSpacsSerializer


    def create(self, request, *args, **kwargs):
        car_data = request.data

        new_car = CarSpacs.objects.create(car_plan= CarPlan.objects.get(id= car_data["car_plan"]),car_brand=car_data["car_brand"], car_model=car_data["car_model"], product_yr=car_data["product_yr"], car_body=car_data["car_body"], engine_type=car_data["engine_type"])

        new_car.save()

        serializer= CarSpacsSerializer(new_car)
        return Response(serializer.data)