#!/usr/bin/python3 
'''
- Work out the first ten digits of the sum 
of the following one-hundred 50-digit numbers.
- Read data from text_13.txt file
'''

from base import Problem 

def read_data():
    '''
    Read one-hundred 50-digit numbers from file 
    '''
    with open('text_13.txt') as f:
        data = f.read() # type(str)
        lines = data.split() # type(list)
        return lines

def first_10_digits_of_sum():
    """
    Return the first 10 digits of the sum
    """
    sum_ = sum([int(i) for i in read_data()])
    return str(sum_)[:10]

class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        output = first_10_digits_of_sum()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(13)
    solution.solve()





