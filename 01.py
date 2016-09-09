#!/usr/bin/python3 
'''
- If we list all the natural numbers below 10 
that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

- Find the sum of all the multiples of 3 or 5 below 1000.
'''

from base import Problem

def sum_multiples():
	'''
	Calculate the sum of all the multiples of 3 or 5 below 1000.
	'''
	return sum(list(range(0, 1000, 3))) + \
        	sum(list(range(0, 1000, 5))) - \
        	sum(list(range(0, 1000, 15)))

class Solution(Problem):
    def solve(self, ):
        print('Solving problem {}'.format(self.number))
        output = sum_multiples()
        print('Result: {}'.format(output))

if __name__ == '__main__':
    solution = Solution(1)
    solution.solve()
    # output: 233168