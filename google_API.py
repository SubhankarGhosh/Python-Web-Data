import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = raw_input('Enter location:')
	if len(address) < 1:
		break
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address})
	print 'Retrieving', url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved', len(data), 'characters'

	try:
		js = json.loads(str(data))
	except:
		js = None
	if 'status' not in js or js['status']!= 'OK':
		print 'Failed to retrieve'
		print data
		continue

	print json.dumps(js, indent = 4)
	location = js["results"][0]["formatted_address"]
	print "Location entered:", location
	latitude = js["results"][0]["geometry"]["location"]["lat"]
	longitude = js["results"][0]["geometry"]["location"]["lng"]
	print "Latitude:", latitude, "\nLongitude:", longitude

#Location entered: Kolkata, West Bengal 700001, India
#Latitude: 22.572646 
#Longitude: 88.363895
#Enter location: