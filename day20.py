import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

swap_count = 0
for i in range(n):

	for i in range(n-1):

		if a[i] > a[i+1]:
			temp = a[i+1]
			a[i+1] = a[i]
			a[i] = temp
			swap_count += 1

	if swap_count == 0:
		break

print "Array is sorted in %d swaps." %swap_count
print "First Element: %d" %a[0] 
print "Last Element: %d" %a[n-1]
