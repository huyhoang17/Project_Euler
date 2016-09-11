#!/usr/bin/python3
'''
- Triangle, pentagonal, and hexagonal numbers are generated 
by the following formulae:

>> Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
>> Pentagonal      Pn=n(3n−1)/2        1, 5, 12, 22, 35, ...
>> Hexagonal       Hn=n(2n−1)      1, 6, 15, 28, 45, ...
- It can be verified that T285 = P165 = H143 = 40755.

- Find the next triangle number that is also pentagonal and hexagonal.
'''

from base import Problem

def tripenhex():
    '''
    Return a the next triangle number that is also pentagonal and hexagonal.
    '''
    T, P, H = 286, 166, 144
    end = 100000
    while True:
        triangular = [x * (x + 1) / 2 for x in range(T, end)]
        pentagonal = [x * (3 * x - 1) / 2 for x in range(P, end)]
        hexagonal = [x * (2 * x - 1) for x in range(H, end)]
        if len(set(triangular) & set(pentagonal) & set(hexagonal)) != 0:
            break
        end += 100000
    return set(triangular) & set(pentagonal) & set(hexagonal)

class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        output = tripenhex()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(45)
    solution.solve()
    # output: 1533776805.0