#!/usr/bin/python3 
'''
- The prime factors of 13195 are 5, 7, 13 and 29.

- What is the largest prime factor of the number 600851475143 ?
'''

from base import Problem

NUM = 600851475143

def largest_prime_factor(n):
	i = 3
	while i < n ** 0.5:
		if n % i == 0:
			n = n // i
		i += 2
	return n

class Solution(Problem):
    def solve(self, input_):
        print('Solving problem {}'.format(self.number))
        output = largest_prime_factor(input_)
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(3)
    solution.solve(NUM)