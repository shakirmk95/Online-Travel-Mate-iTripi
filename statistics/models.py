from django.db import models
import datetime


# Create your models here.
class RideOffer(models.Model):
	origin = models.CharField(max_length = 50)
	destination = models.CharField(max_length = 50)
	weekday = models.IntegerField(max_length =1)
	time = models.TimeField()


class rideSearch(models.Model):
	origin = models.CharField(max_length = 50)
	destination = models.CharField(max_length = 50)
	date_time = models.TimeField()
