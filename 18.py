#!/usr/bin/python3
'''
- Find the maximum total from top to bottom of the triangle

- Read data from file 18_data.txt.
'''

from base import Problem

def read_data():
    with open('18_data.txt') as f:
        data = [l.split() for l in f.readlines()]
        for i in range(len(data)):
        	for j in range(len(data[i])):
        		data[i][j] = int(data[i][j])
        return data

def maximum_total_of_triangle():
	data = read_data()
	max_ = 0
	sum_ = 0
	for i in range(len(data)):
		sum_ = 0
		for j in range(len(data[i])):
			sum_ += data[i][j]
			if max_ < sum_:
				max_ = sum_

	return max_

class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        # output = 
        # print('Result: {}'.format(output))
    
if __name__ == '__main__':
    # solution = Solution(18)
    # solution.solve()
    # output: 23514624000
    print(maximum_total_of_triangle())