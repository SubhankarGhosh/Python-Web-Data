#import socket
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(('http://www.pythonlearn.com', 80))
#sock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')
#import urllib
import re
#fhand = urllib.urlopen('http://www.pythonlearn.com/code/intro-short.txt')
fhand = open('intro-short.txt', 'r')
for line in fhand:
    line = line.strip()
    lst = re.findall('\S*?: (.+)', line)
    if len(lst) != 0:
            print lst[0]
