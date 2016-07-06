def Fib():
    '''
    Fibonanci number
    '''
    a = 1
    b = 2 
    while True:
        yield a
        sum_ = a + b
        a = b
        b = sum_
        
def sum_even_fib():
    '''
    Calculate sum of the the even-valued terms
    '''
    sum_ = 0
    for x in Fib():
        if x >= 4000000:
            break
        if x % 2 == 0:
            sum_ += x
    return sum_

print(sum_even_fib())

'''
output: 4613732
'''