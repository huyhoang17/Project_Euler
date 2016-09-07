#!/usr/bin/python3 
'''
- The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

- Find the sum of all the primes below two million.
'''

import math

from base import Problem

def sum_lst_primes(num):
    # while True:
    lst = [False] * (num)
    lst[2] = True
    lst[3] = True
    lst[5] = True
    lst[7] = True
    for i in range(9, num, 2):
        if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:           
            lst[i] = True
    print(lst[2])
    return lst

def main(num):
    primes = sum_lst_primes(num)
    return (sum([i for i in range(num) if primes[i]]))

class Solution(Problem):
    def solve(self, input_):
        print('Solving problem {}'.format(self.number))
        output = main(input_)
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(10)
    solution.solve(2000000)