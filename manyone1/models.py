from django.db import models

class CarPlan(models.Model):
    plan_name = models.CharField(max_length=50)
    yr_warranty = models.PositiveIntegerField(default = 1)
    finance_yr = models.CharField(max_length=20, default="Unavalable")

    def __str__(self):
        return self.plan_name


class CarSpacs(models.Model):
    car_plan = models.ForeignKey(CarPlan, on_delete=models.SET_NULL, null=True)
    car_brand = models.CharField(max_length=25)
    car_model = models.CharField(max_length=25)
    product_yr = models.CharField(max_length=25)
    car_body = models.CharField(max_length=25)
    engine_type = models.CharField(max_length=25)

    def __str__(self):
        return self.car_brand

