#!/usr/bin/python3 
'''
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

from base import Problem

class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        output = int(str(sum([i**i for i in range(1, 1001)]))[-10:])
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(48)
    solution.solve()