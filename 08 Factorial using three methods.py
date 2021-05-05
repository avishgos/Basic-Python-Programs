# Using For Loop
n = int(input('Enter a number'))
result = 1

for i in range(n,0,-1):
    result = result * i


print('Factorial of n is',result)


# Using Recursion function
def fact(n):
    if n == 0:
        return 1

    else: 
        return n*fact(n-1)

n = int(input('Enter the number'))
result = fact(n)
print('Factorial of',n, 'is',result)


# Using Inbuilt Function

import math
n = int(input('Enter a number'))
result = math.factorial(n)
print('Factorial of',n, 'is',result)
