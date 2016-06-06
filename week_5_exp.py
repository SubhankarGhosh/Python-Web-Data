import urllib
import xml.etree.ElementTree as ET
import re

url = str(raw_input('Enter link to xml:'))
uh = urllib.urlopen(url)
#data = uh.read()

#tree = ET.fromstring(data)

#counts = re.findall('<count>([0-9]+)</count>', url)
sum = 0

for line in uh:
	count = re.findall('<count>([0-9]+)</count>', line)
	if len(count) != 0:
		sum = sum + int(count[0])
print sum