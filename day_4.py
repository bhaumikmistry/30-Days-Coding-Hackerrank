#day4.py

#!/bin/python

import sys
n = int(raw_input().strip())

if n%2==1:
	print 'Weird'
elif (n>=2 and n<=5):
	print 'Not weird'
elif (n> 5 and n<21):
	print 'Weird'
else:
	print 'Not weird'
