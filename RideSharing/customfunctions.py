
def datetime_to_url(date):
	d_string = str(date)
	url = ""
	for letters in d_string:
		if not letters in (" ","-",".",":"):
			url = url+letters

	return url


class Search_Result():        
	def __init__(self,**kwargs):
		# self.id = kwargs ['id']
		self.host_name = kwargs ['host_name']
		self.origin = kwargs ['origin']
		self.destination = kwargs ['destination']
		self.seats = kwargs ['seats']
		self.waypoints =kwargs ['waypoints']
		self.datetime = kwargs ['datetime']
		self.url = kwargs ['url']
		self.image = kwargs['image']
		self.age = kwargs['age']
		self.user_rating = kwargs['user_rating']
		self.make = kwargs['make']
		self.car = kwargs['car']
		self.trans_rating = kwargs['trans_rating']
		self.url_origin =""
		self.url_destination =""

		self.rate = kwargs['rate']
	def value(self):
		ride = {}
	
		ride['host_name'] = self.host_name
		ride['origin'] = self.origin
		ride['destination'] = self.destination
		ride['seats'] = self.seats		
		ride['waypoints'] = self.waypoints
		ride['datetime'] = self.datetime
		ride['url'] = self.url
		ride['image'] = self.image
		ride['age'] = self.age
		ride['user_rating'] = self.user_rating
		ride['trans_rating'] = self.trans_rating
		ride['car']= self.car
		ride['make'] =self.make
		ride['url_origin'] = self.origin.split()[0].split(',')
		ride['url_destination'] = self.destination.split()[0].split(',')
		ride['rate'] = self.rate
		
		return ride
