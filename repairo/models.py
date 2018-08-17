# -*- coding: utf-8 -*-
from django.db import models


class Car(models.Model):
    owner = models.CharField(max_length=100)
    vin_num = models.CharField(max_length=30)
    license_plate = models.CharField(max_length=12)
    serv_hist = models.TextField(null=True, blank=True)
    make = models.CharField(max_length=500)
    model = models.CharField(max_length=500)

    def __str__(self):
        return self.owner


class Repair(models.Model):
    date = models.CharField(max_length=13)
    area_serviced = models.TextField(null=True, blank=True)
    invoice_num = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    # car = models.CharField(max_length=500, null=True, blank=True)
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='repairs', blank=True)

    def __str__(self):
        return self.date


# class Favorite(models.Model):
#     user = models.ForeignKey(
#         'auth.User', related_name='favorites', on_delete=models.CASCADE)
#     car = models.ForeignKey(
#         Car, related_name='favorites', on_delete=models.CASCADE)
# DD
