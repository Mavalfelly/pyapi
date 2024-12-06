from django.db import models

# Create your models here.
class Cars(models.Model):
    car_make=models.CharField(25)
    car_model=models.CharField(25)
    car_color=models.CharField(25)