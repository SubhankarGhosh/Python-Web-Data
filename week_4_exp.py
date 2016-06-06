import urllib
import re
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_200414.html'
html = urllib.urlopen(url) # .read()

#soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
sum = 0
for line in html:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    #print 'Contents:',tag.contents[0]
    #print 'Attrs:',tag.attrs
    lst = re.findall('.*?<span .*?>([0-9]+?)</span>', line)
    if len(lst) != 0:
        sum = sum + int(lst[0])
print sum

