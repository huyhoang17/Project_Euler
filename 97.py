#!/usr/bin/python3 
'''
- The first known prime found to exceed one million digits 
was discovered in 1999, and is a Mersenne prime of the form 
2^6972593−1; it contains exactly 2,098,960 digits. 
- Subsequently other Mersenne primes, of the form 2^p−1, 
have been found which contain more digits.

- However, in 2004 there was found a massive non-Mersenne prime 
which contains 2,357,207 digits: 28433×2^7830457+1.

- Find the last ten digits of this prime number.
'''

from base import Problem

def last_ten_digits():
	return (28433 * (2 ** 7830457) + 1) % 10000000000

class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        output = last_ten_digits()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(97)
    solution.solve()
    # output: 8739992577