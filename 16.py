#!/usr/bin/python3 
'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

- What is the sum of the digits of the number 2^1000 ?
'''

from base import Problem

def main():
	return sum([int(i) for i in list(str(2 ** 1000))])

class Solution(Problem):
    def solve(self, ):
        print('Solving problem {}'.format(self.number))
        output = main()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(16)
    solution.solve()
    # output: 1366