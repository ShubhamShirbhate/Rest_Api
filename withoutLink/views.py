from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Album, Musician,Place
from .serializer import MusicianSerializer, AlbumSerializer, PlaceSerializer

class MusicianListCreateView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    
    

class musicianView(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    #queryset = Album.objects.all()
    serializer_class = MusicianSerializer#,AlbumSerializer
    #serializer_class = AlbumSerializer


    def create(self, request, *args, **kwargs):
        add_data = request.data
        
        musician = Musician.objects.create(musician_name=add_data["musician_name"],instrument=add_data["instrument"])
        musician.save()

        album = Album.objects.create(album_name=add_data["album_name"],relace_date=add_data["relace_date"])
        album.save() 

        place = Place.objects.create(place_name=add_data["place_name"],pincode=add_data["pincode"],date=add_data["date"])
        place.save() 


        serializer = MusicianSerializer(musician) and  AlbumSerializer(album) and PlaceSerializer(place)
        return Response(serializer.data)

class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class PlaceListCreateView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer