from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework import generics
from .serializer import  EmpSerializer
from .models import Emp


class ListCreateView(generics.ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
    

@api_view(['GET'])
def index(request):
    api_urls= {
        'List'      : '/list/',
        'Create'    : '/create/',
        'Details'   : '/details/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def List(request):
    emp = Emp.objects.all()
    serializer = EmpSerializer(emp, many = True)    
    return Response(serializer.data)

@api_view(['POST'])
def Create(request):
    serializer = EmpSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def Details(request, pk):
    emp = Emp.objects.get(id = pk)
    serializer = EmpSerializer(emp, many = False)
    return Response(serializer.data)
 