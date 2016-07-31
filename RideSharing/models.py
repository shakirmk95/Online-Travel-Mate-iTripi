from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class newRide(models.Model):
	host_id = models.ForeignKey(User)
	origin = models.CharField(max_length = 150,blank = False, null = False)
	destination = models.CharField(max_length = 150,blank = False, null = False)
	luggage = models.CharField(max_length = 1, blank =True, null = True)

	seats = models.IntegerField(max_length =1, blank = False,null = False)
	detour = models.CharField(max_length = 3, blank = True, null = True)

	datetime = models.DateTimeField()
	date_published = models.DateField()
	description = models.CharField(max_length = 1000)
	cus_url = models.CharField(max_length = 21)
	seen = models.IntegerField(max_length =3, default =0)
	vehicle_id = models.CharField(max_length = 5,blank = True, null = True)
	rate = models.IntegerField(max_length = 5,blank = True,null = True)

	def detailed_url(self):
		comp_origin = self.origin
		comp_destination = self.destination
		comp_destination = comp_destination.partition(' ')[0].partition(',')[0]
		comp_origin = comp_origin.partition(' ')[0].partition(',')[0]
		return(comp_origin+'/'+self.cus_url+'/'+comp_destination+'/')

	def seat_decrement(self):
		self.seats = self.seats - 1

	def visitor_increment(self):
		self.seen = self.seen + 1

class wayPoints(models.Model):
	ride_id = models.IntegerField(max_length = 50, blank = False, null = False)
	point = models.CharField(max_length = 50)
	alias = models.CharField(max_length = 50)
	reaching_time = models.CharField(max_length = 25)
	rate = models.IntegerField(max_length = 5,blank = True,null = True)


	def waypointname(self):
		return self.point


class requestedUsers(models.Model):
	ride_id = models.ForeignKey(newRide, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name ='user_id')
	host_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name ='host_id')
	status = models.CharField(max_length = 1,default  ='N')
	time_of_approval = models.DateTimeField(blank = True,null = True)
	cus_url = models.CharField(max_length = 21)