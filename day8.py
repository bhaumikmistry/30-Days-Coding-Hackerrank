# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input().strip())
arr = dict((raw_input().strip().split(' ')) for i in range(n))

# arr={}
# arr =  [map(str,raw_input().strip().split(' ')) for x in range(n)]


# for q in query:
# 	tureval = 0
# 	if q in arr:
# 		print q+"=%s" % arr.get(q)
# 	else:
# 		print "Not found"
while True:
 	try:
		query = [raw_input()]#for i in range(n)]
		# if query in arr:
		print query
		print query +"=%s" % arr.get(query)
		# else:
		 	# print 'Not found'
	except:
 		exit(0)

# while True:
#     try:
# 		query = [raw_input()]#for i in range(n)]
#         if query in arr:
# 			print q+"=%s" % arr.get(q)
#         else:
#             print('Not found')
#     except:
#         break

# print arr
# for q in query:
# 	trueval = 0;
# 	for i in range(0,n):
# 		if arr[i][0] == q:
# 			print (q+'='+str(arr[i][1]))
# 			trueval = 1
# 	if trueval == 0:
# 		print "Not found"

#  tis will not work for larger data like 10^5