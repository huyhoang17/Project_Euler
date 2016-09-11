#!/usr/bin/python3
'''
- The nth term of the sequence of triangle numbers is given by:
>> tn = ½n(n+1)
so the first ten triangle numbers are:

>> 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

- By converting each letter in a word to a number corresponding 
to its alphabetical position and adding these values we form a 
word value. For example: 
>> the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.
'''

from string import ascii_uppercase

from base import Problem

def read_data():
    '''
    Read data from files. Convert string to list and return values.
    '''
    with open('42_data.txt') as f:
        data = f.read().split(',')
        return data

def word_point(str_):
    sum_ = 0
    for i in str_:
        if i in ascii_uppercase:
            sum_ += ascii_uppercase.index(i) + 1
    return sum_

def triangle_words():
    lst = [int(0.5 * i * (i + 1)) for i in range(1, 27)]
    data = read_data()
    count = 0
    for i in data:
        if word_point(i) in lst:
            count += 1
    return count

class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        output = triangle_words()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(42)
    solution.solve()
    # output: 162