from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from RideSharing.models import newRide


class UserNotifications(models.Model):
	target_user = models.CharField(max_length = 50)
	message = models.CharField(max_length = 256)
	has_read = models.BooleanField(default = False)

	def __str__(self):
		return self.message


class UserImage(models.Model):
	image = models.ImageField(upload_to='profile_pic',default ='default.jpg')
	user_id = models.OneToOneField(User,primary_key=True)

	def saveresizedimage(self, force_insert=False, force_update=False):
		super(UserImage, self).save(force_insert, force_update)
		if self.user_id is not None:
			previous = UserImage.objects.get(user_id=self.user_id)
			if True:			
				image1 = Image.open(self.image.path)
				# console.log(self.image.path)				
				image1 = image1.resize((96, 96), Image.ANTIALIAS)
				image1.show()
				image1.save(self.image.path)

class UserProfile(models.Model):
	user_id = models.OneToOneField(User,primary_key=True)
	mobile = models.CharField(max_length = 15)#
	phone_visiblity = models.CharField(max_length=1, default='Y')
	yob = models.IntegerField(max_length = 4,blank = True,null = True)#
	work = models.CharField(max_length= 120)
	bio = models.CharField(max_length = 1000)#
	add1 = models.CharField(max_length = 250,default = "")
	add2 = models.CharField(max_length = 250,default = "")
	zip_code = models.CharField(max_length = 8)
	city = models.CharField(max_length = 30)
	country = models.CharField(max_length = 20)
	province = models.CharField(max_length = 20)
	user_rating = models.IntegerField(max_length = 1,default= 0)
	job_title = models.CharField(max_length = 200,null = True, blank = True)
	organisation = models.CharField(max_length = 200, null = True, blank = True)
	original_image_url = models.CharField(max_length = 128,null = True,blank = True)
	thumbnail_image_url = models.CharField(max_length = 128,null = True,blank = True)


class Transport(models.Model):
	COMFORT_CHOICE  = (('B','Basic'),('N','Normal'),('L','Luxuary'),('C','Comfortable'))
	# user_id = models.ForeignKey(User)
	user_id = models.IntegerField(max_length = 15)
	make = models.CharField(max_length = 15)
	car = models.CharField(max_length = 15)
	varient = models.CharField(max_length = 15)
	color = models.CharField(max_length = 15,blank = True,null = True,default="Green")
	comfort = models.CharField(max_length = 15,choices = COMFORT_CHOICE,blank = True,null = True)
	seats = models.IntegerField(max_length = 1)
	trans_rating = models.IntegerField(max_length = 1,default = 1,blank = True,null = True)
	image = models.ImageField(upload_to='car/%Y/%m/%d',default ='default.jpg',blank = True,null = True)
	def __str__(self):
		user = User.objects.get(id = self.user_id)
		return user.first_name+" " + self.car


	def detailedname(self):
		return self.make + " " + self.car


class UserRating(models.Model):
	user_id = models.IntegerField(max_length = 100)
	voters_id = models.IntegerField(max_length = 100)
	rating = models.IntegerField(max_length = 1)


class CarRating(models.Model):
	car_id = models.IntegerField(max_length = 100)
	voters_id = models.IntegerField(max_length = 100)
	rating = models.CharField(max_length = 1)

class RideReview(models.Model):
	ride_id = models.CharField(max_length = 100)
	voters_id = models.CharField(max_length = 100)
	review_descriprion = models.CharField(max_length = 256)

class Messages(models.Model):
	sender = models.ForeignKey(User, related_name = "sender",on_delete=models.CASCADE)
	reciever = models.ForeignKey(User, related_name = "reciever",on_delete=models.CASCADE)
	message = models.CharField(max_length = 1000)
	has_read = models.IntegerField(max_length = 1,default = 0)
	sent_time = models.DateTimeField(blank = True,null = True)
	read_time = models.DateTimeField(blank = True,null = True)


	ride_link = models.ForeignKey(newRide,related_name = "ride_id",on_delete=models.CASCADE)
	cus_url = models.CharField(max_length = 21)