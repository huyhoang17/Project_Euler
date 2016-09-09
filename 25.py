#!/usr/bin/python3 
'''
- What is the index of the first term 
in the Fibonacci sequence to contain 1000 digits?
'''

from base import Problem

def index_1000_fibo():
	"""
	Print index of the first term in the fibo sequence 
	Break if length of number == 1000
	"""
	count = 0
	a, b = 0, 1
	while True:
		a, b = b, a + b
		# yield(a)
		count += 1
		if len(str(a)) == 1000:
			return count
			break

class Solution(Problem):
    def solve(self, ):
        print('Solving problem {}'.format(self.number))
        output = index_1000_fibo()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(25)
    solution.solve()
    # output: 4782