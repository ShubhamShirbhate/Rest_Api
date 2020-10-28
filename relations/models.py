from django.db import models

class Paradigm(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Languages(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Proggrammer(models.Model):
    name = models.CharField(max_length=50)
    language = models.ManyToManyField(Languages)

    def __str__(self):
        return self.name
