# project euler: sublit 15
def factorial(n): 
	'''
	Find the factorial n! of a number
	'''
	result = 1
	for i in range(1, n + 1): 
		result *= i
	return result

# calculate the number of routes of a (n / 2) grid
# combination: a k-combination of a set S is a subset of k distinct elements of S
# k-combination of a set S = n! / ( k! * (n - k)! )
output = factorial(40) / (factorial(20) * factorial(20))

print(output) #137846528820

