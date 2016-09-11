#!/usr/bin/python3
'''
- We shall say that an n-digit number is pandigital 
if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

- What is the largest n-digit pandigital prime that exists?
'''

from base import Problem

def is_prime(num):
    for i in range(2, int(num ** 0.5)):
        if num % i == 0: 
            return False
    return True

def is_pandigital(num):
    return set([int(i) for i in str(num)]) == set(range(1, len(str(num)) + 1))

def prime_pandigital():
    for i in range(7654321, 0, -2):
        if i % 5 != 0 and i % 7 != 0 and is_prime(i) and is_pandigital(i):
            return i

class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        output = prime_pandigital()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(41)
    solution.solve()
    # output: 