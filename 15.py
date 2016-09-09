#!/usr/bin/python3 
'''
- Starting in the top left corner of a 2×2 grid, and only being 
able to move to the right and down, there are exactly 6 routes 
to the bottom right corner.   

- How many such routes are there through a 20×20 grid?
'''

from base import Problem 

def factorial(n): 
	'''
	Find the factorial n! of a number
	'''
	result = 1
	for i in range(1, n + 1): 
		result *= i
	return result

def main(n):
	'''
	calculate the number of routes of a (n / 2) grid
	combination: a k-combination of a set S is a subset of k distinct elements of S
	k-combination of a set S = n! / ( k! * (n - k)! )
	'''
	return factorial(2 * n) / (factorial(n) * factorial(n))

class Solution(Problem):
    def solve(self, input_):
        print('Solving problem {}'.format(self.number))
        output = main(input_)
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(15)
    solution.solve(20)	
    # output: 137846528820