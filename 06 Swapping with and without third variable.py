# Using third variable

a = int(input('Enter the first number'))
b = int(input('Enter the second number'))

temp = a
a = b
b = temp
print('After swapping')
print('Value of a',a)
print('Value of b',b)


# Without using third variable
a = int(input('Enter the first number'))
b = int(input('Enter the second number'))

a = a+b
b = a-b
a = a-b
print('After swapping')
print('Value of a',a)
print('Value of b',b)