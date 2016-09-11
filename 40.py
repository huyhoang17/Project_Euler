#!/usr/bin/python3
'''
- An irrational decimal fraction is created by concatenating 
the positive integers:

0.123456789101112131415161718192021...

- It can be seen that the 12th digit of the fractional part is 1.

- If d_n represents the n_th digit of the fractional part, find the 
value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
'''

from base import Problem

def product_decimal_fraction(n):
    '''
    Return the value of the following expression:
    d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
    '''
    str_ = ''
    for i in range(1, 200000):
        str_ += str(i)
    result = 1
    start = '1'
    for i in range(n):
        result *= int(str_[int(start) - 1])
        start += '0'
    return result

class Solution(Problem):
    def solve(self, input_):
        print('Solving problem {}'.format(self.number))
        output = product_decimal_fraction(input_)
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(40)
    # 1-10-100-1000-10000-100000-1000000
    solution.solve(7)
    # output: 210