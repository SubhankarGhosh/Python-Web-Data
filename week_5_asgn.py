import urllib
import xml.etree.ElementTree as ET

url = str(raw_input('Enter link to xml:'))
uh = urllib.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)

counts = tree.findall('.//count')

sum = 0

for count in counts:
	sum = sum + int(count.text)

print sum