import urllib
import twurl
import json
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
while True:
	acct = raw_input('Enter a Twitter Account:')
	if len(acct)<1:
		break
	url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
	print 'Retrieving', url
	connection = urllib.urlopen(url)
	data = connection.read()
	headers = connection.info.dict	#Create a dictionary from the Header data
	print 'Remaining', headers['x-rate-limit-remaining']
	js = json.loads(data)
	print json.dumps(js, indent = 4)

	print js['users']