#!/usr/bin/python3
'''
- What is the greatest product of four adjacent numbers 
in the same direction (up, down, left, right, or diagonally) 
in the 20×20 grid?

- Read data from 11_data.txt.
'''

from base import Problem

def read_data():
    with open('11_data.txt') as f:
        data = [l.split() for l in f.readlines()]
        for i in range(20):
        	for j in range(20):
        		data[i][j] = int(data[i][j])
        return data

def greatest_product_adjacent_numbers():
	data = read_data()
	max_ = 0
	for i in range(20):
		for j in range(16):
			pro = data[i][j] * data[i][j + 1] * \
					data[i][j + 2] * data[i][j + 3]
			if max_ < pro:
				max_ = pro
			pro = data[j][i] * data[j + 1][i] * \
					data[j + 2][i] * data[j + 3][i]
			if max_ < pro:
				max_ = pro
	
	for i in range(16):
		for j in range(16):
			pro = data[i][j] * data[i + 1][j + 1] * \
					data[i + 2][j + 2] * data[i + 3][j + 3]
			if max_ < pro:
				max_ = pro

	for i in range(3, 20):
		for j in range(16):
			pro = data[i][j] * data[i - 1][j + 1] * \
					data[i - 2][j + 2] * data[i - 3][j + 3]
			if max_ < pro:
				max_ = pro
	
	return max_

class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        output = greatest_product_adjacent_numbers()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(11)
    solution.solve()
    # output: 70600674