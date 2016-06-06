# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
import re
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
pos = int(raw_input('Enter position - '))
no_of_times = int(raw_input('Enter number of times - '))
lst = re.findall('.+_(.+)[.]', url)
#print lst
#name = 
for i in range(no_of_times):
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        tag = tags[pos-1]
        name = tag.contents[0]
        lst.append(str(name))
        url = tag.get('href')
print lst[len(lst)-1]
