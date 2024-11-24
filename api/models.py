from django.db import models



# Create your models here.

class Vehicle(models.Model):

    name=models.CharField(max_length=200)

    vehicle_number=models.CharField(max_length=200)

    owner_type=(
        ("first-owner","first-owner"),
        ("second-owner","second-owner"),
    )

    owner=models.CharField(max_length=200,choices=owner_type,default="fisrt-owner")

    running_km=models.FloatField()

    price=models.CharField(max_length=200)

    description=models.CharField(max_length=200)

    fuel_type=(
        ("petrol","petrol"),
        ("diesel","diesel"),
        ("electric","electric"),
    )

    fuel_item=models.CharField(max_length=200,choices=fuel_type,default="petrol")

    def __str__(self) -> str:

        return  self.name


        

