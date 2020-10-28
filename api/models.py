from django.db import models

# Create your models here.

class Emp(models.Model):
    title   = models.CharField(max_length=20)
    age     = models.IntegerField()
    phone   = models.CharField(max_length=11)
    address = models.TextField()


    def __str__(self):
        return self.title

