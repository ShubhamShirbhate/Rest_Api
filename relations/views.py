from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ParadigmSerializer, LanguageSerializer, ProggrammerSerializer
from .models import Paradigm, Proggrammer, Languages


class LanguagesView(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProggrammerViews(viewsets.ModelViewSet):
    queryset = Proggrammer.objects.all()
    serializer_class = ProggrammerSerializer
