#!/usr/bin/python3 
'''
- Surprisingly there are only three numbers that can be written 
as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
- As 1 = 1**4 is not a sum it is not included.

- The sum of these numbers is 1634 + 8208 + 9474 = 19316.

- Find the sum of all the numbers that can be written as the sum 
of fifth powers of their digits.
'''

from base import Problem

def sum_of_all_numbers_digits():
	return sum([i for i in range(2, 9 ** 5 * 6 + 1) 
		if i == sum([int(j)**5 for j in str(i)])])

class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        output = sum_of_all_numbers_digits()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(30)
    solution.solve()