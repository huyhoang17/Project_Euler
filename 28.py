#!/usr/bin/python3
'''
- Starting with the number 1 and moving to the right 
in a clockwise direction a 5 by 5 spiral is formed as follows:

21.  22  23  24  25.
20   7.  8   9.  10
19   6   1.  2   11
18   5.  4   3.  12
17.  16  15  14  13.

- It can be verified that the sum of the numbers on the diagonals is 101.

>> 1 + 3 + 5 + 7 + 9 + 13 + 17 + 21 + 25 = 101

- What is the sum of the numbers on the diagonals in a 1001 by 
1001 spiral formed in the same way?
'''

from base import Problem

def sum_diagonals_spiral_formed(n):
    '''
    Calculate sum of the numbers on the diagonals in a n by 
    n spiral formed (n is odd numbers).
    '''
    sum_ = 1
    count = 1
    for i in range(3, n + 1, 2):
        # i, x = 3, 9; i, x = 4,16; ...
        x = i ** 2
        # 3(y) = 9(x) - 1.6; 13(y) = 25(x) - 2.6; ...
        y = x - 6 * count
        count += 1
        # 9 + 3 = 7 + 5; 25 + 13 = 21 + 17; ...
        sum_ += 2 * (x + y)
    return sum_

class Solution(Problem):
    def solve(self, input_):
        print('Solving problem {}'.format(self.number))
        output = sum_diagonals_spiral_formed(input_)
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(28)
    solution.solve(1001)
    # output: 669171001