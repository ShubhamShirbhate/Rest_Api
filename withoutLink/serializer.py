from rest_framework import serializers
from .models import Album, Musician, Place


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ('id', 'musician_name', 'instrument')

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'album_name','relace_date')


class PlaceSerializer(serializers.ModelSerializer):
    date = serializers.ReadOnlyField()
    class Meta:
        model = Place
        fields = ('id', 'place_name','pincode','date')