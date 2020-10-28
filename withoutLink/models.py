from django.db import models

class Musician(models.Model):
    musician_name = models.CharField(max_length=20)
    instrument = models.CharField(max_length=20)

    def __str__(self):
        return self.musician_name

class Album(models.Model):
    album_name = models.CharField(max_length=10)
    relace_date = models.CharField(max_length=20)

    def __str__(self):
        return self.album_name

class Place(models.Model):
    place_name = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.place_name