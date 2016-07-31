from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset

from django.template import loader, Context
from django.template.loader import get_template
import datetime
from django.views.decorators.csrf import csrf_exempt
from usermanagement.models import UserNotifications, UserProfile, Messages, UserImage, Transport

from django.template.context import RequestContext

from RideSharing.models import newRide, requestedUsers
from usermanagement.forms import ImageUploadForm, TransportForm
from django.db.models import Q
from RideSharing.customfunctions import datetime_to_url
from itripi.settings import MEDIA_URL
from PIL import Image
import StringIO
import django.core.files
import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.conf import settings

import uuid

dic = {}

CURRENT_DATE_TIME  =datetime.datetime.now()


@login_required
def rideApproval(request,cus_url):
	if request.method == 'POST':
		try:
			ride = requestedUsers.objects.get(cus_url = cus_url)
			ride.status = 'Y'
			ride.time_of_approval = datetime.datetime.now()

			ride.save()
			temp_newride = newRide.objects.get(id= ride.ride_id_id)
			temp_newride.seat_decrement()
			temp_newride.save()
			print(ride.host_id_id)
			
		except:
			print("in Catch")
			pass
	return HttpResponseRedirect('/usermanagement/messages/'+cus_url)


@login_required
def messages(request,cus_url):
	variables ={}
	if request.method =='POST':
		mess = request.POST.get('message')
		instance = Messages.objects.filter(cus_url = cus_url).values()[0]
		# print(instance['sender_id'],instance['reciever_id'])
		sender = User.objects.get(id = request.user.id)
		x = Messages.objects.create(message = mess,sender = request.user,
			reciever = User.objects.get(id = instance['sender_id']),
			cus_url = instance['cus_url'],
			ride_link_id = instance['ride_link_id'],
			sent_time=datetime.datetime.now())

	try:	
		messages = Messages.objects.filter(cus_url = cus_url).values()
		ride_l = messages[0]['ride_link_id']
		ride_l = newRide.objects.get(id = ride_l)

		if ride_l.host_id_id == request.user.id:
			variables['unhide'] = True
		else:
			variables['unhide'] = False


		if messages[0]['sender_id'] == request.user.id or messages[0]['reciever_id'] == request.user.id:
			User1_id = messages[0]['sender_id']
			User2_id = messages[0]['reciever_id']
			User1 = User.objects.get(id = User1_id)
			User2 = User.objects.get(id = User2_id)
			User1_profile = UserProfile.objects.get(user_id = User1)
			User2_profile = UserProfile.objects.get(user_id = User2)
			User1_image = UserImage.objects.get(user_id = User1)
			User2_image = UserImage.objects.get(user_id = User2)
			
	except:
		print(" i am in except")
		pass

	Requested_users = requestedUsers.objects.get(user_id= User1,ride_id_id = messages[0]['ride_link_id'],host_id = User2,cus_url = cus_url)
	for each_message in messages:
		sender_details = {}
		if each_message['sender_id'] == User1_id:
			sender_details['sender_name'] = User1.first_name+ ' ' + User1.last_name
			sender_details['image'] = User1_image.image
			each_message['sender_id'] = sender_details
			variables['page_title'] = ""
		else:
			sender_details['sender_name'] = User2.first_name+ ' ' + User2.last_name
			sender_details['image'] = User2_image.image
			each_message['sender_id'] = sender_details


	if request.user == User1:
		variables['sender_user'] = User2
		variables['sender_profile'] = User2_profile
		variables['sender_image'] = User2_image.image

		variables['age'] = 0

	else:
		variables['sender_user'] = User1
		variables['sender_profile'] = User1_profile
		variables['sender_image'] = User1_image.image
		variables['age'] = 0
	
	#CURRENT_DATE_TIME.year - User1_profile.yob
	variables['messages'] = messages
	variables['cus_url'] = messages[0]['cus_url']
	variables['Requested_users'] = Requested_users
	variables['ride_profile'] = newRide.objects.get(id = messages[0]['ride_link_id'])
	variables['page_title'] = "Messages"+ " " + variables['sender_user'].first_name +" "+variables['sender_user'].last_name
	variables['MEDIA_URL'] = MEDIA_URL
	return render(request,"messages.html",variables)
0
@login_required
def mailbox(request):
	variables = {}
	if request.method == 'POST':
		message = request.POST.get('message')
		cus_url = request.POST.get('cus-url')
		ride = newRide.objects.get(cus_url = cus_url)
		prev_message = Messages.objects.filter(Q(sender = request.user,ride_link = ride,reciever = ride.host_id)|Q(reciever = request.user,ride_link = ride,sender = ride.host_id))
		print(len(list(prev_message)),"len")
		if len(list(prev_message)) == 0:
			print(datetime.datetime.now())
			print("i Am in IF")
			newMessgae = Messages.objects.create(sender = request.user,
				reciever = ride.host_id,
				message = message,
				sent_time = datetime.datetime.now(),
				cus_url = datetime_to_url(datetime.datetime.now()),
				ride_link = ride)
			requestedUsers.objects.create(ride_id= ride,
				user_id = request.user,
				host_id = ride.host_id,
				cus_url = newMessgae.cus_url)

		else:
			print("i Am in Else")
			newMessgae = Messages.objects.create(sender = request.user,
				reciever = ride.host_id,
				message = message,
				sent_time = datetime.datetime.now(),
				cus_url = prev_message[0].cus_url,
				ride_link = ride)

		return HttpResponseRedirect("/usermanagement/messages/"+newMessgae.cus_url+'/')
	message_list = []
	try:
		url_list = Messages.objects.filter(Q(reciever = request.user)|Q(sender = request.user)).values('cus_url').distinct()
		for each_url  in url_list:
			x = Messages.objects.filter(cus_url = each_url['cus_url']).values()
			message_list.append(x[len(list(x))-1])
	except:
		pass

	for each in message_list:
		print(each['sender_id'], each['reciever_id'],each['id'])

		each['sender_id'] = User.objects.get(id = each['sender_id'])
		each['reciever_id'] = User.objects.get(id = each['reciever_id'])
		print(each['sender_id'], each['reciever_id'])

	variables['url_list'] = url_list
	variables['page_title'] = "Inbox"
	variables['messages'] = message_list


	return render(request,"mailbox.html",variables)


@csrf_exempt
def user_login_status(request):
	return render_to_response (request.user.is_authenticated())



@csrf_exempt
def user_login(request):
	variables = {}		
	logged_in = False		
	if request.method == 'POST':		
		username = request.POST.get('username')
	 	password = request.POST.get('password')
	 	user = authenticate(username = username, password = password)		
		if user:		 	
		 	if user.is_active:		 		
		 		login(request,user)	
		 		userNotifications = UserNotifications.objects.all().filter(target_user = request.user.id).values()
		 		variables['userNotifications'] = userNotifications
		 		variables['user'] = user	 		
		 	return HttpResponseRedirect('/home/')

	elif request.user.is_authenticated:
		pass
		# return HttpResponseRedirect('/home/')

	return render(request,"login.html",variables)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect("/home/")

def home(request):
	incompleted = False
	profile = None
	if request.user.is_authenticated:
		if request.user.is_active:
			try:
				profile = UserProfile.objects.get(user_id = request.user)
				
			except UserProfile.DoesNotExist:
				profile = UserProfile.objects.create(user_id = request.user,
					phone_visiblity='Y',
					thumbnail_image_url = "thumbnail_profile_pic/default_thumb.jpg")
				

   	context = RequestContext(request,
                           {'request': request,
                            'user': request.user,
                            'profile':profile})
  	return render_to_response('home.html',
                             context_instance=context)



@csrf_exempt
def newUser(request):
	name = request.POST.get('name')
	email = request.POST.get('email')
	password1 = request.POST.get('password1')
	password2 = request.POST.get('password2')
	newUser = User.objects.create(username = email,email = email, password = password1, first_name = name)
	newUser.set_password(newUser.password)
 	newUser.save()
 	Notifications.objects.create(user_id = newUser.id)
 	UserProfile.objects.create(user_id = newUser.id)
 	usernotif = userNotifications.objects.create(user_id = newUser.id, category = 'W',description= '', has_read = 0,created_date_time = datetime.datetime.now())
	usernotif.description = " Welcome to WhyAlone, Now You can start exploring your rides from the Search"
	usernotif.save()

 	return HttpResponse("Your Account Has been Successfully Created")


@csrf_exempt
def userNameAvailable(request):
	variables ={}
	if request.method == 'POST':		
		email = request.POST.get('email')
		print(email)
		if email == "":
			return render_to_response("enterusername.html")
		else:
			try:
				print("Try")
				userExist = User.objects.get(username = email)

				return render_to_response("user_already_exists.html")

			except User.DoesNotExist:
				variables['email'] = email
				print("Catch")
				return render_to_response("user_name_available.html",variables)

@login_required
def userProfile(request):
	if request.user.is_active:
		if request.method == 'POST':
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			mobile = request.POST.get('mobile')
			yob = request.POST.get('yob')
			bio = request.POST.get('bio')
			mobile_privacy = request.POST.get('mobile_privacy')
			current_user = User.objects.get(id = request.user.id)
			current_user.first_name = first_name
			current_user.last_name = last_name
			current_user.email = email
			current_user.save()
			current_profile = UserProfile.objects.get(user_id = request.user)
			current_profile.mobile = mobile
			current_profile.yob = yob
			current_profile.bio = bio
			current_profile.save()	
		try:
	
			user_details = UserProfile.objects.get(user_id = request.user.id)
		except UserProfile.DoesNotExist:
			user_image = UserImage.objects.create(user_id = request.user)
			user_details = UserProfile.objects.create(user_id = request.user)
		try:
			user_image = UserImage.objects.get(user_id = request.user)
		except UserImage.DoesNotExist:
			user_image = UserImage.objects.create(user_id = request.user)
		try:
			cars = Transport.objects.filter(user_id = request.user.id)

		except:
			cars = []

		image_upload_form = ImageUploadForm()
		transportform = TransportForm()

	variables = {}
	variables['cars'] = cars
	variables['transportform'] = transportform
	variables['MEDIA_URL'] = MEDIA_URL
	variables['image_upload_form'] = image_upload_form
	variables['user_image'] = user_image
	variables['user'] = User.objects.get(id = request.user.id)
	variables['active_profile'] = "active"
	variables['profile'] = UserProfile.objects.get(user_id = request.user.id)
	print(variables['profile'])
	return render(request,"settings.html",variables)

def handle_uploaded_image(request,i): 
    imagefile  = StringIO.StringIO(i.read())
    imageImage = Image.open(imagefile)
    (width, height) = imageImage.size
    resizedImage = imageImage.resize((200, 90))
    resizedImage.show()
    imagefile = StringIO.StringIO()
    resizedImage.save(imagefile,'JPEG')   
    filename = str(request.user.username)+'.jpg'   
    imagefile = open(os.path.join('media',filename), 'w')
    resizedImage.save(imagefile,'JPEG')
    content = django.core.files.File(imagefile)   
    my_object = UserImage()
    my_object.user_id = request.user
    my_object.image.save(filename, content)
    imagefile.close()

@login_required
def imageuploader(request):
	def store_original_profile_pic_s3(filename,content):
		conn = S3Connection(settings.AWS_ACCESS_KEY_ID,settings.AWS_SECRET_ACCESS_KEY)
		bucket = conn.get_bucket('itripi')
		k = Key(bucket)
		k.key = 'original_profile_pic/'+filename+'.jpg'
		k.set_contents_from_string(content)
		k.set_acl("public-read")

	def store_thumbnail_profile_pic_s3(filename,original_file):
		imagefile = StringIO.StringIO(original_file)
		im = Image.open(imagefile)
		(width,height) = im.size
		im = im.resize((width/10,height/10), Image.ANTIALIAS)
		temp_im = StringIO.StringIO()
		im.save(temp_im,"JPEG")
		conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
		b = conn.get_bucket("itripi")
		k = Key(b)
		k.key = 'thumbnail_profile_pic/'+filename+ '.jpg'
		temp_im.seek(0)
		k.set_contents_from_file(temp_im)
		k.set_acl("public-read")


	if request.method == "POST":
		file = request.FILES['image']
		content = file.read()
		filename = uuid.uuid4().hex
		store_thumbnail_profile_pic_s3(filename,content)
		store_original_profile_pic_s3(filename,content)

		y = UserProfile.objects.filter(user_id = request.user)
		y.update(original_image_url = 'original_profile_pic/'+filename+'.jpg',thumbnail_image_url = 'thumbnail_profile_pic/'+filename+'.jpg')

	return HttpResponseRedirect('/usermanagement/profile/')
# @login_required
# def imageuploader(request):
# 	# def store_original_profile_pic_s3(filename,content):
# 	# def store_original_profile_pic_s3(filename,content):
# 		# pass
# 	# 	conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
# 	# 	b = conn.get_bucket("itripi")
# 	# 	k = Key(b)
# 	# 	k.key = 'uploaded_profile_pic/'+uuid.uuid4().hex +'.jpg'
# 	# 	k.set_contents_from_string(content)
# 	# 	k.set_acl("public-read")

#     if request.method == 'POST':
#     	print("I am in Uploader")


#         # form = ImageUploadForm(request.POST, request.FILES)        
#         # if form.is_valid():
#         #     newdoc = UserImage(user_id = 1,image = request.FILES['image'])
#         #     image = request.FILES['image']
#         #     # handle_uploaded_image(request,request.FILES['image'])
#         file = request.FILES['image']
#         content = file.read()
#         store_original_profile_pic_s3(file,content)


#         userinstance = User.objects.get(id = request.user.id)
#         x = UserImage(user_id = userinstance, image = request.FILES['image'])
#         x.saveresizedimage()
        
# 	return HttpResponseRedirect('/usermanagement/profile/')




@login_required
def transportadder(request):
	variables = {}
	if request.method == 'POST':
		
		form = TransportForm(request.POST,request.FILES)
		if form.is_valid():

			newCar = Transport(image = request.FILES['image'],
				user_id = request.user.id,
				varient = request.POST.get('varient'),
				car = request.POST.get('car'),
				make = request.POST.get('make'),
				seats = request.POST.get('seats'),
				color = request.POST.get('color')
				)

			newCar.save()
			variables['success'] = "Your New Car Has Been Successfully Added to iTripi"
	return HttpResponseRedirect('/usermanagement/profile/')
	return render(request,"settings.html",variables)


@login_required
def workProfile(request):
	if request.method =='POST':
		job_title = request.POST.get('job_title')
		organisation = request.POST.get('organisation')
		
	pass


@login_required  		
def userPostal(request):
	if request.user.is_active:
		if request.method == 'POST':
			add1 = request.POST.get('add_line1')
			add2= request.POST.get('add_line2')
			city = request.POST.get('city')
			province = request.POST.get('province')
			zip_code = request.POST.get('zip_code')
			country = request.POST.get('country')
			print(add1,add2,city,province,zip_code,country)
			current_profile = UserProfile.objects.get(user_id = request.user.id)
			print(current_profile)
			current_profile.add1 = add1
			current_profile.add2 = add2
			current_profile.city = city
			current_profile.country = country
			current_profile.zip_code = zip_code
			current_profile.province = province
			current_profile.save()
		else:
			try:
				user_details = UserProfile.objects.get(user_id = request.user.id)
				
			except UserProfile.DoesNotExist:
				user_details = UserProfile.objects.create(user_id = request.user.id)

				print(user_details)
				print("i Went to except")
	

	return HttpResponseRedirect('/usermanagement/profile/')


