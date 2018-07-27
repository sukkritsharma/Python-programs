from cs50 import get_int

while True:
	n = get_int("Height: ")
	if n>=0 and n<24:
	    break

for i in range(n):
	a=i+1
	print(" "*(n-a) + "#"*(a) + "#")