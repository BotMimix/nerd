# Create a program that simplifies fractions entered by the user.
# The program should prompt the user for a numerator and denominator
# and output the simplified fraction.

from math import *

def euclid_algo(x, y, verbose=True):
	if x < y:
		return euclid_algo(y, x, verbose)
	print()
	while y != 0:
		if verbose: print('%s = %s * %s + %s' % (x, floor(x/y), y, x % y))
		(x, y) = (y, x % y)
	
	if verbose: print(int(num/x),"/",int(den/x))
	return x
    

num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

euclid_algo(num, den);