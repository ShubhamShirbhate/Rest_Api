from django.db import models


class Carplan(models.Model):
    plan_name = models.CharField(max_length=20)
    car_warranty = models.PositiveIntegerField(default=1)
    finance_plan = models.CharField(max_length=20)


    def __str__(self):
        return self.plan_name


class Carspace(models.Model):
    car_name    = models.CharField(max_length=20)
    car_model   = models.CharField(max_length=20)
    production_yr = models.IntegerField()
    car_plan = models.ForeignKey(Carplan, on_delete=models.CASCADE)


    def __str__(self):
        return self.car_name