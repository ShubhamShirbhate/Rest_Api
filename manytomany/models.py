from django.db import models


class Module(models.Model):
    module_name = models.CharField(max_length=100)
    duration    = models.IntegerField()
    class_room  = models.IntegerField()

    def __str__(self):
        return self.module_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField()
    grade = models.IntegerField()
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return self.name