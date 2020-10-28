from django.shortcuts import render
from .models import Carspace, Carplan
from rest_framework import viewsets
from .serializers import CarspaceSerializer
from rest_framework.response import Response

class CarView(viewsets.ModelViewSet):
    queryset = Carspace.objects.all()
    serializer_class = CarspaceSerializer


   
    def create(self, request, *args, **kwargs):
        add_car = request.data

        new_car = Carspace.objects.create(car_plan=Carplan.objects.get(plan_name = add_car['car_plan']), car_name=add_car['car_name'], car_model=add_car['car_model'], production_yr=add_car['production_yr'])
        new_car.save()
    
        serilizer = CarspaceSerializer(new_car)
        return Response(serializer.data)
    '''
    
    def create(self, request, *args, **kwargs):
        car_data = request.data

        new_car = Carspace.objects.create(
                            car_plan=Carplan.objects.get(id=car_data["car_plan"]),
                            #car_brand=car_data["car_brand"],
                            #car_name=car_data['car_name'],
                            #car_model=car_data["car_model"],
                            car_name=car_data['car_name'],
                            car_model=car_data['car_model'],
                            production_yr=car_data['production_yr']
                            #production_year=car_data["production_year"],
                            #car_body=car_data["car_body"], 
                            #engine_type=car_data["engine_type"]
                            )

        new_car.save()

        serializer = CarspaceSerializer(new_car)

        return Response(serializer.data)
     '''
    
