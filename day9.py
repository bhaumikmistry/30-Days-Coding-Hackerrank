# day9.py

def Factorial(n):
	if n == 1:
		return 1;
	else:
		return n * Factorial(n-1)

n = int(raw_input());
f = Factorial(n);

print f