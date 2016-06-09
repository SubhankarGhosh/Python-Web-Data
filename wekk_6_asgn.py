import json
import urllib

sum = 0
url = raw_input('Enter - ')
uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(str(data))
length = len( js["comments"])

for i in range(length):
	num = js["comments"][i]["count"]
	sum = sum + num

print sum