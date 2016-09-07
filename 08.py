#!/usr/bin/python3 
'''
- Find the thirteen adjacent digits in the 1000-digit number 
that have the greatest product. 

- What is the value of this product?
'''

from base import Problem

def read_data():
	'''
	Read 1000-digit number from file
	'''
	with open('8_data.txt') as f:
		data = ''.join([i for i in (f.read()).split()])
		return data # type(str) len(1000)

def multi_thirteen(str_num):
	'''
	Find the product of thirteen number 
	'''
	product = 1
	for i in range(0, 13):
		product *= int(str_num[i])
	return product

def thirteen_digits_greatest_product():
	'''
	Find the thirteen adjacent digits in the 1000-digit number 
	that have the greatest product
	'''
	data = read_data()
	start_index, end_index = 0, 13
	result = 0
	for i in range(len(data) - 13):
		str_ = data[start_index:end_index]
		start_index += 1
		end_index += 1
		product = multi_thirteen(str_)
		if product > result:
			result = product
	return result


class Solution(Problem):
    def solve(self):
        print('Solving problem {}'.format(self.number))
        output = thirteen_digits_greatest_product()
        print('Result: {}'.format(output))
    
if __name__ == '__main__':
    solution = Solution(8)
    solution.solve()