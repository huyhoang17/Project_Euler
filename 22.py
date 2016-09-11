#!/usr/bin/python3 
'''
- Begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position 
in the list to obtain a name score.

- For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

- What is the total of all the name scores in the file?
'''

from base import Problem

from string import ascii_uppercase

def words_point(names):
	result = sum([ascii_uppercase.find(i) + 1 for i in names 
			if i in ascii_uppercase])
	return result

def read_data():
	with open('22_data.txt') as f:
		data = f.read().split(',')
		return sorted(data)

def score():
	data = read_data()
	result, output = 0, 0
	for name in data: 
		result = words_point(name) * (data.index(name) + 1)
		output += result  
	return output

class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        output = score()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(22)
    solution.solve()
	# output = 871198282