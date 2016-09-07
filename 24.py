#!/usr/bin/python3 
'''
- A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

- What is the millionth lexicographic permutation 
of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from itertools import permutations

from base import Problem

def millionth_lexicographic_permutation(num):
    '''
    - Find the millionth lexicographic permutation 
    of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
    '''
    return ''.join([str(i) for i in list(permutations(list(range(0, 10))))[num]])

class Solution(Problem):
    def solve(self, input_):
        print('Solving problem {}'.format(self.number))
        output = millionth_lexicographic_permutation(input_ - 1)
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(24)
    solution.solve(1000000)