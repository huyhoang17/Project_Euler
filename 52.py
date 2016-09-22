#!/usr/bin/python3
'''
- It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

- Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, 
and 6x, contain the same digits.
'''

from base import Problem

def check_same_digits(num):
	for i in range(2, 7):
		if sorted(list(str(num))) != sorted(list(str(num * i))):
			return False
	return True

def smallest_same_digits(num):
	for i in range(100, num):
		if check_same_digits(i):
			return i

class Solution(Problem):
    def solve(self, input_):
        print('Solving problem {}'.format(self.number))
        output = smallest_same_digits(input_)
        print('Result: {}'.format(output))

if __name__ == '__main__':
    solution = Solution(52)
    solution.solve(10**6)
    # output: 142857