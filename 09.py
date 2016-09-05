#!/usr/bin/python3 
# -*- coding: utf-8 -*-
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
	a^2 + b^2 = c^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""

def pythagorean():
	lst = [i for i in range(1, 1000)]
	ans = 0
	for a in lst:
		for b in lst:
			c = 1000 - (a + b)
			if a ** 2 + b ** 2 - c ** 2 == 0:
				ans = a * b * c
	return ans

if __name__ == '__main__':
	print(pythagorean())


