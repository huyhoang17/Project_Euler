#!/usr/bin/python3 
'''
- A palindromic number reads the same both ways. 
- The largest palindrome made from the product of two 2-digit numbers 
is 9009 = 91 × 99.

- Find the largest palindrome made from the product of two 3-digit numbers.
'''

from base import Problem

def check_palirome(n):
	'''
	Check palirome number .
	'''
	if str(n) == str(n)[::-1]:
		return True
	else:
		return False

def max_palirome():
	'''
	Find the max palirome number i
	'''
	palirome = []
	for i in range(999, 99, -1):
		for j in range(999, 99, -1):
			if check_palirome(i * j):
				palirome.append(i * j)
	return max(palirome)

class Solution(Problem):
    def solve(self, ):
        print('Solving problem {}'.format(self.number))
        output = max_palirome()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(4)
    solution.solve()
    # 906609