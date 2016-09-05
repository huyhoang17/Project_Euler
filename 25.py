#!/usr/bin/python3 
# -*- coding: utf-8 -*-
"""
What is the index of the first term 
in the Fibonacci sequence to contain 1000 digits?
"""
def index_1000_fibo():
	"""
	print index of the first term in the fibo sequence 
	break if length of number == 1000
	"""
	count = 0
	a, b = 0, 1
	while True:
		a, b = b, a + b
		# yield(a)
		count += 1
		if len(str(a)) == 1000:
			return count
			break

if __name__ == '__main__':
	print(index_1000_fibo())