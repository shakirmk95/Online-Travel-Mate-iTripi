from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from RideSharing.models import newRide,wayPoints
from statistics.models import RideOffer,rideSearch
import datetime
from django.contrib.auth.models import User
from customfunctions import datetime_to_url, Search_Result
from usermanagement.models import UserProfile, Transport, UserImage
from itripi.settings import MEDIA_URL
from django.template import RequestContext

variables = {}
CURRENT_DATETIME = datetime.datetime.now()

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def poll(request):
    return render(request,"poll.html")

@login_required
def offer(request):
	variables = {}
	if request.method == 'POST':
		ride_datetime = request.POST.get('datetime')
		vehicle_id = request.POST.get('car')


		if datetime_to_url(ride_datetime) > datetime_to_url(CURRENT_DATETIME):
			origin = request.POST.get('det-origin')
			destination = request.POST.get('det-destination')
			waypoints = request.POST.getlist('det-waypoints')
			seats = request.POST.get('seatSelector')
			description = request.POST.get('description')
			luggage = request.POST.get('luggage')
			server_date_time = datetime.datetime.now()
			vehicle_id = request.POST.get('car')
			fare_list = request.POST.getlist('price')
	
			
			agg_sum = 0
			agg_price_list =[]
		
			for each_fare in fare_list:
				agg_sum = agg_sum  + int(each_fare)
				agg_price_list.append(agg_sum)
				#print(agg_sum, each_fare)

			
			url = datetime_to_url(server_date_time)
			this_ride = newRide.objects.create(host_id = request.user,
				origin =origin,
				destination = destination,
				seats = seats,
				datetime = str(ride_datetime),
				description= description,
				cus_url = url,
				luggage = luggage,
				vehicle_id = vehicle_id,
				date_published = server_date_time.date(),
				rate = agg_price_list[-1])
			counter = 0
			for waypoint in waypoints:
				if(len(waypoint)>1):
					wayPoints.objects.create(ride_id = this_ride.id, point = waypoint, alias ="N",reaching_time = str(ride_datetime),rate = agg_price_list[counter])
					counter = counter + 1

			return HttpResponseRedirect('/ridesharing/rides/'+this_ride.cus_url +"/blank/blank/")

		else:
			variables['datetime_error'] = "Enter An Upcoming Date"
			return render(request,"offer.html",variables)


	
	else:
		transport = Transport.objects.filter(user_id = request.user.id).values()
		variables['transport'] = transport
		return render(request,"offer.html",variables)

@csrf_exempt
def ride_search(request):
	Search_result_list = []
	variables['MEDIA_URL'] = MEDIA_URL	
	origin = request.GET.get('origin')
	destination = request.GET.get('destination')
	if origin:
		origin = origin.split()[0].split(',')[0]
	if destination:
		destination = destination.split()[0].split(',')[0]
	try:
		result = newRide.objects.all().values().filter(origin__istartswith = origin, destination__istartswith = destination,datetime__gt = datetime.datetime.now(),seats__gte = 1).values()		
		for res in result:
			temp_waypoint_list = []
			try:
				waypoint = wayPoints.objects.filter(ride_id = res['id']).values()
				for point in waypoint:				
					temp_waypoint_list.append(point['point'])				
			except:
				pass
	
			host = User.objects.get(id = res['host_id_id'])
			try:
				temp = Transport.objects.get(id = res['vehicle_id'])
				make = temp.make
				car = temp.car
				trans_rating = temp.trans_rating

			except:
				make  = ""
				car = ""
				trans_rating = ""

			host_profile = UserProfile.objects.get(user_id = res['host_id_id'])
			if host_profile.yob == None or host_profile.yob == 0:
				host_profile.yob = CURRENT_DATETIME.year

			image_profile = UserImage.objects.get(user_id = res['host_id_id'])
			searchobject = Search_Result(host_name = host.first_name+" "+ host.last_name,
				waypoints = temp_waypoint_list,
				origin = res['origin'],
				destination = res['destination'],
				datetime = res['datetime'],
				seats = res['seats'],
				url = res['cus_url'],
				image = image_profile.image,
				age = int(CURRENT_DATETIME.year) -int(host_profile.yob),
				user_rating = range(0,5),
				make= make,
				car = car,
				trans_rating = range(0,0),
				rate = res['rate'])		
			Search_result_list.append(searchobject)
	except newRide.DoesNotExist:
		result = []
	finally:		
		try:
			temp_origin = wayPoints.objects.filter(point = origin)			
			for i in temp_origin:		
				try:
					temp_waypoint_list = []
					temp_destination = wayPoints.objects.get(point = destination,id__gt = i.id,ride_id = i.ride_id)
					temp_rate = temp_destination.rate - i.rate					
					temp_original_ride = newRide.objects.get(id = temp_destination.ride_id)	
					try:
						temp_car = Transport.objects.get(id = temp_original_ride.vehicle_id)						
					except:						
						temp_car = ""				
					try:									
						temp_waypoints_waypoints = wayPoints.objects.filter(id__gt = i.id,id__lt = temp_destination.id)						
						if not len(list(temp_waypoints_waypoints)):							
							raise wayPoints.DoesNotExist						
						for j in temp_waypoints_waypoints.values():										
							temp_waypoint_list.append(j['point'])
						
					except wayPoints.DoesNotExist:
						temp_waypoints_waypoints =[]		
					
					finally:						
						parent_ride = newRide.objects.get(id = temp_destination.ride_id)						
						ride_host = User.objects.get(id = parent_ride.host_id_id)											
						profile = UserProfile.objects.get(user_id = parent_ride.host_id)			

						image_profile = UserImage.objects.get(user_id = parent_ride.host_id)
						searchobject = Search_Result(host_name = ride_host.first_name + " " +ride_host.last_name,
							waypoints = temp_waypoint_list,
							origin = origin,
							destination = destination,
							datetime = parent_ride.datetime,
							seats = parent_ride.seats,
							url = parent_ride.cus_url,
							image = image_profile.image,
							age= "50",
							user_rating = range(0,5),
							make = temp_car.make,
							car = temp_car.car,
							trans_rating = range(0,temp_car.trans_rating),
							rate = temp_rate)
						print("Parent ride is",parent_ride)
						
					
						Search_result_list.append(searchobject)

				except:
					pass

		except wayPoints.DoesNotExist:
			pass

			#print("Non NOn ")
	variables['result'] = result

	count = len(list(result))

	final_result = []
	for i in Search_result_list:
		final_result.append(i.value())
	
	variables['origin'] = origin
	variables['destination'] = destination

	variables['Search_Result'] = final_result	
	return render(request,"search.html",variables)
	# return render(request,"offer.html")


def details(request,rideid,origin,destination):
	variables = {}
	variables['rideid'] =  rideid
	ride = newRide.objects.get(cus_url = rideid)
	try:
		waypoints = wayPoints.objects.filter(ride_id = ride.id)
		waypoints = waypoints.values()
	except wayPoints.DoesNotExist:
		waypoints = []

	

	variables['origin'] =  ride.origin
	variables['destination'] = ride.destination
	variables['rate'] = 0
	init_price = 0
	final_price = 0
	temp_waypoint_id = 0
	if (origin =='blank') & (destination=='blank'):

		variables['rate'] = ride.rate

	elif origin == 'blank':
		#print("origin is not der")
		if destination.lower() in ride.destination.lower():
			variables['rate'] = ride.rate
		else:
			for each in waypoints:
				if destination.lower() in each['point'].lower():
					variables['rate'] = each['rate']
					break

	elif destination == 'blank':
		
		#print("Destiantion is not dere")
		if origin.lower() in ride.origin.lower():
			variables['rate'] = ride.rate
		else:
			for each in waypoints:
				if origin.lower() in each['point'].lower():
					variables['rate'] = ride.rate - each['rate']
					break


	else:
		#print(origin, ride.origin, destination, ride.destination)
		if origin.lower() in ride.origin.lower() and destination.lower() in ride.destination.lower():
			variables['rate'] = ride.rate
		else:			
			for each in waypoints:
				if origin.lower() in each['point'].lower():
					#print(each['point'])
					init_price = each['rate']
					temp_waypoint_id = each['id']
					break

			for each in waypoints:
				if destination.lower() in each['point'].lower():
					#print(each['point'])
					final_price = each['rate']
					variables['rate'] = final_price - init_price
					break


	try:
		car = Transport.objects.get(id = ride.vehicle_id)
	except:	
		car = None

	owner = User.objects.get(id = ride.host_id_id)
	try:

		profile = UserProfile.objects.get(user_id = owner)
	except:
		profile = UserProfile.objects.create(user_id = owner,
			phone_visiblity = 'Y',
			yob = None,
			bio = "",
			thumbnail_image_url = "thumbnail_profile_pic/default_thumb.jpg",
			)
	if profile.yob == None or profile.yob == 0:
		profile.yob = 0
	else:
		profile.yob = 2016-profile.yob	
	user = User.objects.get(id = ride.host_id_id)
	# user_image = UserImage.objects.get(user_id = owner)
	variables['car'] = car
	variables['waypoints'] = waypoints
	variables['ride'] = ride
	variables['owner'] = owner
	variables['profile'] = profile
	variables['host_user'] = user
	# variables['user_image'] = user_image
	variables['MEDIA_URL'] = MEDIA_URL	
	return render(request,"details.html",variables)



@csrf_exempt
def rideOffer(request):
	variables = {}
	origin = request.POST.get('det-origin')
	destination = request.POST.get('det-destination')
	waypoints = request.POST.getlist('waypoints')
	ride_datetime = request.POST.get('datetime')
	seats = request.POST.get('seats')
	description = request.POST.get('description')
	server_date_time = datetime.datetime.now()
	url = datetime_to_url(server_date_time)	
	if not (request.user.is_authenticated()):
		#print("User Not is_authenticated")
		return HttpResponse("DJER001")

	elif(origin ==""):
		#print("No Origin Selected")
		return HttpResponse("DJER002")
	elif(destination==""):
		#print("No Destination")
		return HttpResponse("DJER003")
	else:
		this_ride = newRide.objects.create(host_id = request.user.id,
			origin =origin,
			destination = destination,
			seats = 5,
			datetime = str(ride_datetime),
			description= description,
			cus_url = url,
			date_published = server_date_time.date())
		for waypoint in waypoints:
			if(len(waypoint)>1):
				wayPoints.objects.create(ride_id = this_ride.id, point = waypoint, alias ="N",reaching_time = str(ride_datetime))
		variables['this_ride'] = this_ride.detailed_url()
		return render_to_response("success.html",variables)

@csrf_exempt
def rideSubmission(request):
	variables = {}
	if request.user.is_active:
		if request.method == 'POST':
			variables['origin'] = request.POST.get('origin')
			variables['destination'] = request.POST.get('destination')
			variables['luggage'] =  request.POST.get('luggageSelector')
			make =  request.POST.get('carMake')
			return_trip = request.POST.get('returnTripSel')
			waypoints = request.POST.get('waypoints')
			ride_details = request.POST.get('rideDetailsTA')
			date = request.POST.get('date')
			seats = request.POST.get('seatSelector')
			detour = request.POST.get('detourSelector')
			delay = request.POST.get('delaySelector')
			variables['date'] = request.POST.get('date')

			if return_trip == "on":
				return_trip = 1
			else:
				return_trip = 0
			
			current_date = datetime.datetime.now()
			url = datetime_to_url(current_date)
			newRide.objects.create(host_id = request.user.id,
				origin =variables['origin'],
				destination=variables['destination'],
				luggage=variables['luggage'],
				return_trip = return_trip,
				return_trip_id = 1,
				starting_time = datetime.datetime.now().time(),

				reaching_time = "15:02:12",
				seats =sea,
				detour = 5,
				delay = 5,
				date = variables['date'],
				url = url)

			#print("Added To DataBase")
	else:
		pass
		#print("user is not active")

@csrf_exempt
def rideSearch(request):
	variables = {}
	origin = request.POST.get('origin')
	destination = request.POST.get('destination')
	rides = newRide.objects.all().filter(origin = origin,destination = destination).values()
	result_nos = len(list(rides))
	variables['rides'] = rides
	variables['result_nos'] = result_nos
	for i in range (0,result_nos):
		variables['rides'][i]['host'] = User.objects.get(id =variables['rides'][i]['host_id']).first_name	
	return render_to_response("ridesearch.html",variables)

