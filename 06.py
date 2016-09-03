'''
Find the difference between the sum of the squares 
of the first one hundred natural numbers and the square of the sum.
'''

def sum_of_the_squares(n):
	'''
	1**2 + 2**2 + ... + 10**2 = 385
	'''
	return sum([i**2 for i in range(1, n + 1)])

def square_of_the_sum(n):
	'''
	(1 + 2 + ... + 10)**2 = 55**2 = 3025
	'''
	return (sum([i for i in range(1, n + 1)]))**2

if __name__ == '__main__':
	n = 100
	# print(square_of_the_sum(n) - sum_of_the_squares(n))
	#one-liner
	print((sum([i for i in range(1, n + 1)]))**2 - 
		sum([i**2 for i in range(1, n + 1)]))