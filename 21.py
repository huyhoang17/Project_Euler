#!/usr/bin/python3 
'''
- Cap so than thien =)

- Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

- For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

- Evaluate the sum of all the amicable numbers under 10000.
'''

from base import Problem

def proper_diviors(num):
    '''
    Find all proper divisors of number
    '''
    sum_ = 0
    for i in range(1, num):
        if num % i == 0:
            sum_ += i
    return sum_

def sum_of_all_amicable_number(num):
    '''
    Evaluate the sum of all the amicable numbers under 'num'
    '''
    result = 0
    for i in range(1, num):
        temp = proper_diviors(i)
        if proper_diviors(temp) == i and temp != i:
            result += temp
    return result

class Solution(Problem):
    def solve(self, input_):
        print('Solving problem {}'.format(self.number))
        output = sum_of_all_amicable_number(input_)
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(21)
    solution.solve(10000)
    # output: 31626