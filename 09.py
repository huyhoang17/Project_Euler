#!/usr/bin/python3 
'''
- A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
	a^2 + b^2 = c^2
- There exists exactly one Pythagorean triplet for which a + b + c = 1000.

- Find the product abc.
'''

from base import Problem

def pythagorean():
	'''
	Return the product of abc if (a, b, c) is a set of 3 natural numbers
	and a+ b + c == 1000.
	'''
	lst = [i for i in range(1, 1000)]
	ans = 0
	for a in lst:
		for b in lst:
			c = 1000 - (a + b)
			if a ** 2 + b ** 2 - c ** 2 == 0:
				ans = a * b * c
	return ans

class Solution(Problem):
    def solve(self, ):
        print('Solving problem {}'.format(self.number))
        output = pythagorean()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(9)
    solution.solve()
    # output: 31875000