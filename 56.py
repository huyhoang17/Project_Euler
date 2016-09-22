#!/usr/bin/python3
'''
- A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

- Considering natural numbers of the form, ab, where a, b < 100, 
what is the maximum digital sum?
'''

from base import Problem

def sum_digital_number(num):
	sum_ = 0
	for i in str(num):
		sum_ += int(i)
	return sum_

def maximum_digital_sum():
	return max([sum_digital_number(i**j) 
		for i in range(1, 101) 
		for j in range(1, 101)])

class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        output = maximum_digital_sum()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(56)
    solution.solve()
    # output: 972 
