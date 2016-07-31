from RideSharing.models import newRide, wayPoints

origin = "Kottam"
destination = "Chertala"


temp  = wayPoints.objects.all().filter(point = "kottayam")
point_id = []
journey_id = []
for i in temp:
	p_id = i.id
	j_id = j.ride_id
	point_id.append(p_id)
	journey_id.append(j_id)

count = len(point_id)
way_point_object = []
for j in range(0,count):
	way_point_temp = wayPoints.objects.all().filter(point = "Chertala", ride_id = journey_id[j], id__gte = point_id[j])
	way_point_object.append(way_point_temp)

print(way_point_object) 