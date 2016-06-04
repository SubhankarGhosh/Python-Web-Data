import re
fh = open('regex_sum_200409.txt','r')
lst = list()
sum = 0
for line in fh:
	line = line.strip()
	y = re.findall('[0-9]+', line)
	lst = lst + y
for str in lst:
	num = int(str)
	sum = sum + num
print sum
