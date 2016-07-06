#project euler: submit 22
import string

def sums_alphabet(names):
	'''
	scoring a string
	'''
	alphabet = string.ascii_uppercase
	result = 0
	results = sum([alphabet.find(i) + 1 for i in names if i in alphabet])
	return(results)

filename = "p022_names.txt"

#open file with mode "read"
f = open(filename, "r")

# read data from file 
data = f.read()

# list
data = data.split(",")
data.sort()

# convert list from string 
data_output = ','.join(data)
#print(data_output)
f.close()

# open file again 
f = open(filename, "w")
# write data into file 
f.write(data_output)

# print(data)

f.close()

def score(data):
	'''
	the total of all the name scores in the file
	'''
	result = 0
	output = 0
	for name in data: 
		result = sums_alphabet(name) * (data.index(name) + 1)
		output += result  
	return output

print(score(data))

# output = 871198282












