#!/usr/bin/python3 
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

from base import Problem

def factorial(num):
    '''
    Return product of n!.
    '''
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sum_of_the_digits(num):
    '''
    The sum of the digits in the number 'num' (100)
    '''
    return sum([int(i) for i in str(factorial(num))])

class Solution(Problem):
    def solve(self, input_):
        print('Solving problem {}'.format(self.number))
        output = sum_of_the_digits(input_)
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(20)
    solution.solve(100)
    # output: 648