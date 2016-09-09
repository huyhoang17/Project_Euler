#!/usr/bin/python3 
'''
- Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. By starting with 1 and 2, 
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

- By considering the terms in the Fibonacci sequence whose values 
do not exceed four million, find the sum of the even-valued terms.
'''

from base import Problem 

def fibonanci():
    '''
    Return the sequence of Fibonanci number.
    '''
    a = 1
    b = 2 
    while True:
        yield a
        sum_ = a + b
        a = b
        b = sum_
        
def sum_even_fib():
    '''
    Calculate sum of the the even-valued terms.
    '''
    sum_ = 0
    for x in fibonanci():
        if x >= 4000000:
            break
        if x % 2 == 0:
            sum_ += x
    return sum_

class Solution(Problem):
    def solve(self, ):
        print('Solving problem {}'.format(self.number))
        output = sum_even_fib()
        print('Result: {}'.format(output))

if __name__ == '__main__':
    solution = Solution(2)
    solution.solve()
    # output: 4613732