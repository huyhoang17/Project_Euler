'''
Find the largest palindrome made from the product of two 3-digit numbers.
'''
def check_palirome(n):
	'''
	check palirome number 
	'''
	if str(n) == str(n)[::-1]:
		return True
	else:
		return False

def max_palirome():
	'''
	find the max palirome number i
	'''
	palirome = []
	for i in range(999, 99, -1):
		for j in range(999, 99, -1):
			if check_palirome(i * j):
				palirome.append(i * j)
	return max(palirome)

if __name__ == '__main__':
	print(max_palirome())