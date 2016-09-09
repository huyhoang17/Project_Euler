#!/usr/bin/python3 
'''
- The decimal number, 585 = 10010010012 (binary), 
is palindromic in both bases.

- Find the sum of all numbers, less than one million, 
which are palindromic in base 10 and base 2.

- (Please note that the palindromic number, in either base, 
may not include leading zeros.)
'''

from base import Problem

def check_db_palindromes(n):
    '''
    Return True if n is palindromic in both bases: 2 and 10 
    '''
    # bin(n) -- type(str)
    if str(n) == str(n)[::-1]:
        if bin(n)[2:] == bin(n)[2:][::-1]:
            return True
    return False

def sum_db_palindromic():
    '''
    Calculate sum of all palindromic number under 10**6
    '''
    return sum([i for i in range(1, 10**6) if check_db_palindromes(i)])

class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        output = sum_db_palindromic()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(36)
    solution.solve()
    # output: 872187