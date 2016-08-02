# day10.py
#  decimal to binary and counting longest chain of 1

a =[]
def Decbin(n):
	while n > 0:	
		rem = n % 2;
		a.insert(0, rem)
		n= n//2;
		# print n;
	return a;

def consi(n):
	count = 1
	newcount = 0
	for i in range(0,len(n)-1):
		k=1
		# print 'i val'
		# print i
		while k>0:
			if n[i] == 1 and n[i+1] == 1:
				count = count + 1
				# print len(n)
				# print count
				# print i
				if i == len(n)-2:
					k=0
				else:
					i=i+1

			else:
				k = 0
		if count > newcount:
			newcount = count
		count = 1;
	return newcount
				


			



n = int(raw_input())
ns = Decbin(n)
x = consi(ns)



print x
# print ns