#!/usr/bin/python3 
'''
Find the difference between the sum of the squares 
of the first one hundred natural numbers and the square of the sum.
'''

from base import Problem

def sum_of_the_squares(n):
	'''
	Return the sum of the squares of the first n natural numbers
	1**2 + 2**2 + ... + 10**2 = 385
	'''
	return sum([i**2 for i in range(1, n + 1)])

def square_of_the_sum(n):
	'''
	Return the square of the sum of the first n natural numbers.
	(1 + 2 + ... + 10)**2 = 55**2 = 3025
	'''
	return (sum([i for i in range(1, n + 1)]))**2

def main(n):
	return square_of_the_sum(n) - sum_of_the_squares(n)

class Solution(Problem):
    def solve(self, input_):
        print('Solving problem {}'.format(self.number))
        output = main(input_)
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(6)
    solution.solve(100)
    # output: 25164150