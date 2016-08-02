#!/bin/python
# 2D array and hour glass.


import sys


arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

def findsum(arr):	
	oldsum = -63;
	for i in range (0,4):
		for j in range (0,4):
			sum1 = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr [i+1][j+1] +  arr[i+2][j] + arr [i+2][j+1] + arr[i+2][j+2]
			if sum1 > oldsum:
				oldsum = sum1
	return oldsum

print(findsum(arr))
