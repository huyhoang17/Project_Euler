#!/usr/bin/python3
'''
- 2520 is the smallest number that can be divided by each 
of the numbers from 1 to 10 without any remainder.

- What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?
'''

from base import Problem

def check_divisible(i, n):
	'''
	Return True if i is evenly divisible 
	by all of the numbers from 11 to n - 1.
	'''
	lst = list(range(11, n))
	for item in lst:
		if i % item != 0:
			return False
	return True

def smallest_divisible(n):
	'''
	Return the smallest positive number that is evenly divisible 
	by all of the numbers from 11 to n - 1.
	'''
	i = n
	while True:
		i += n
		if check_divisible(i, n):
			return i

class Solution(Problem):
    def solve(self, input_):
        print('Solving problem {}'.format(self.number))
        output = smallest_divisible(input_)
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(5)
    solution.solve(20)
    # output: 232792560